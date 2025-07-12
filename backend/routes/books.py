# DEFINES ENDPOINTS FOR MANAGING A USERS BOOK
# TO ADD A BOOK TO A USERS PERSONAL READING LIST
import falcon
from sqlalchemy import text
from db.connection import engine

class UserBooksResource:

    # ADD A BOOK TO MY READING LIST
    def on_post(self, req, resp):
        data = req.media
        user_id = data.get('user_id')
        title = data.get('title')
        authors = data.get('authors')
        thumbnail_url = data.get('thumbnail_url')
        status = data.get('status', 'NOT_STARTED')
        progress = data.get('progress', 0)
        rating = data.get('rating')
        notes = data.get('notes')

        if not user_id or not title or not authors:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id, title, and authors are required'}
            return

        try:
            with engine.begin() as conn:
            # Step 1: Find or insert book
                select_book = text("SELECT id FROM books WHERE title = :title AND authors = :authors")
                result = conn.execute(select_book, {'title': title, 'authors': authors}).fetchone()
                if result:
                    book_id = result.id
                else:
                    insert_book = """
                    INSERT INTO books (title, authors, thumbnail_url, google_book_id)
                    VALUES (:title, :authors, :thumbnail_url, :google_book_id)
                    RETURNING id
                    """
                    result = conn.execute(text(insert_book), {
                        'title': title,
                        'authors': authors,
                        'thumbnail_url': thumbnail_url,
                        'google_book_id': data.get('google_book_id')
                    })
                    book_id = result.fetchone().id

            # Step 2: Add to user_books if not already there
                    insert_user_book = """
                    INSERT INTO user_books (user_id, book_id, status, progress, rating, notes)
                    VALUES (:user_id, :book_id, :status, :progress, :rating, :notes)
                    ON CONFLICT (user_id, book_id) DO NOTHING
                    """

                    conn.execute(text(insert_user_book), {
                        'user_id': user_id,
                        'book_id': book_id,
                        'status': status,
                        'progress': progress,
                        'rating': rating,
                        'notes': notes
                    })

            resp.status = falcon.HTTP_201
            resp.media = {'message': 'Book added to reading list', 'book_id': book_id}

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to add book', 'details': str(e)}

    # def on_post(self, req, resp):
    #     data = req.media
    #     user_id = data.get('user_id')
    #     book_id = data.get('book_id')

    #     if not user_id or not book_id:
    #         resp.status = falcon.HTTP_400
    #         resp.media = {'error': 'user_id and book_id are required'}
    #         return

    #     # Default values
    #     status = data.get('status', 'not_started')
    #     progress = data.get('progress', 0)
    #     rating = data.get('rating', None)
    #     notes = data.get('notes', None)

    #     # THIS ADDS A NEW ROW INTO THE user_books TABLE
    #     # IF THAT USER ALREADY ADDED THAT BOOK IT DOES NOTHING
    #     insert_query = """
    #     INSERT INTO user_books (user_id, book_id, status, progress, rating, notes)
    #     VALUES (:user_id, :book_id, :status, :progress, :rating, :notes)
    #     ON CONFLICT (user_id, book_id) DO NOTHING;
    #     """

    #     try:
    #         with engine.begin() as conn:
    #             conn.execute(text(insert_query), {
    #                 'user_id': user_id,
    #                 'book_id': book_id,
    #                 'status': status,
    #                 'progress': progress,
    #                 'rating': rating,
    #                 'notes': notes
    #             })
    #         resp.status = falcon.HTTP_201
    #         resp.media = {'message': 'Book added to reading list'}
    #     except Exception as e:
    #         resp.status = falcon.HTTP_500
    #         resp.media = {'error': 'Failed to add book', 'details': str(e)}
    # # GETS A USERS READING LIST
    # def on_get(self, req, resp):
    #     user_id = req.get_param('user_id')
    #     status = req.get_param('status')  # optional

    #     if not user_id:
    #         resp.status = falcon.HTTP_400
    #         resp.media = {'error': 'user_id is required'}
    #         return

    #     base_query = """
    #     SELECT ub.*, b.title, b.authors, b.thumbnail_url
    #     FROM user_books ub
    #     JOIN books b ON ub.book_id = b.id
    #     WHERE ub.user_id = :user_id
    #     """
    #     params = {'user_id': user_id}

    #     if status:
    #         base_query += " AND ub.status = :status"
    #         params['status'] = status

    #     try:
    #         with engine.begin() as conn:
    #             result = conn.execute(text(base_query), params)
    #             books = []
    #             for row in result:
    #                 #  # Debug: see full row mapping
    #                 books.append(dict(row._mapping))
    #         resp.status = falcon.HTTP_200
    #         resp.media = books
    #     except Exception as e:
    #         resp.status = falcon.HTTP_500
    #         resp.media = {'error': 'Failed to fetch reading list', 'details': str(e)}
    # UPDATES INFO SENT BY THE USER
    def on_patch(self, req, resp):
        data = req.media
        user_id = data.get('user_id')
        book_id = data.get('book_id')

        if not user_id or not book_id:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id and book_id are required'}
            return

        status = data.get('status')
        progress = data.get('progress')
        rating = data.get('rating')
        notes = data.get('notes')

        update_fields = []
        params = {'user_id': user_id, 'book_id': book_id}

        if status is not None:
            update_fields.append("status = :status")
            params['status'] = status
        if progress is not None:
            update_fields.append("progress = :progress")
            params['progress'] = progress
        if rating is not None:
            update_fields.append("rating = :rating")
            params['rating'] = rating
        if notes is not None:
            update_fields.append("notes = :notes")
            params['notes'] = notes

        if not update_fields:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'No fields provided to update'}
            return

        update_query = f"""
        UPDATE user_books
        SET {', '.join(update_fields)}
        WHERE user_id = :user_id AND book_id = :book_id
        """

        try:
            with engine.begin() as conn:
                result = conn.execute(text(update_query), params)
                if result.rowcount == 0:
                    resp.status = falcon.HTTP_404
                    resp.media = {'error': 'No such book in user reading list'}
                    return

            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Reading progress updated successfully'}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to update reading progress', 'details': str(e)}
    # DELETE a book from user's reading list
    def on_delete(self, req, resp):
        data = req.media
        user_id = data.get('user_id')
        book_id = data.get('book_id')

        if not user_id or not book_id:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id and book_id are required'}
            return

        delete_query = """
        DELETE FROM user_books
        WHERE user_id = :user_id AND book_id = :book_id
        """

        try:
            with engine.begin() as conn:
                result = conn.execute(text(delete_query), {'user_id': user_id, 'book_id': book_id})
                if result.rowcount == 0:
                    resp.status = falcon.HTTP_404
                    resp.media = {'error': 'Book not found in user reading list'}
                    return

            resp.status = falcon.HTTP_200
            resp.media = {'message': 'Book removed from reading list'}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to remove book', 'details': str(e)}
