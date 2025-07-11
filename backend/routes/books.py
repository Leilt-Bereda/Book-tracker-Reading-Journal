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
        book_id = data.get('book_id')

        if not user_id or not book_id:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id and book_id are required'}
            return

        # Default values
        status = data.get('status', 'not_started')
        progress = data.get('progress', 0)
        rating = data.get('rating', None)
        notes = data.get('notes', None)

        # THIS ADDS A NEW ROW INTO THE user_books TABLE
        # IF THAT USER ALREADY ADDED THAT BOOK IT DOES NOTHING
        insert_query = """
        INSERT INTO user_books (user_id, book_id, status, progress, rating, notes)
        VALUES (:user_id, :book_id, :status, :progress, :rating, :notes)
        ON CONFLICT (user_id, book_id) DO NOTHING;
        """

        try:
            with engine.begin() as conn:
                conn.execute(text(insert_query), {
                    'user_id': user_id,
                    'book_id': book_id,
                    'status': status,
                    'progress': progress,
                    'rating': rating,
                    'notes': notes
                })
            resp.status = falcon.HTTP_201
            resp.media = {'message': 'Book added to reading list'}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to add book', 'details': str(e)}
    # GETS A USERS READING LIST
    def on_get(self, req, resp):
        user_id = req.get_param('user_id')
        status = req.get_param('status')  # optional LETS THE USER FILTER BY THEIR STATUS

        if not user_id:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id is required'}
            return

        base_query = """
        SELECT * FROM user_books
        WHERE user_id = :user_id
        """
        params = {'user_id': user_id}

        if status:
            base_query += " AND status = :status"
            params['status'] = status

        try:
            with engine.begin() as conn:
                result = conn.execute(text(base_query), params)
                books = [dict(row._mapping) for row in result]
            resp.status = falcon.HTTP_200
            resp.media = books
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to fetch reading list', 'details': str(e)}
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
