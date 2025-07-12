import falcon
from db.connection import engine
from sqlalchemy import text
import os
import openai
import requests
import re

openai.api_key = os.getenv('OPENAI_API_KEY')
GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes"

class RecommendationsResource:
    def on_get(self, req, resp):
        user_id = req.get_param('user_id')
        if not user_id:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'user_id is required'}
            return

        # Step 1: Fetch user's reading list books
        query = """
        SELECT b.title, b.authors
        FROM user_books ub
        JOIN books b ON ub.book_id = b.id
        WHERE ub.user_id = :user_id
        """
        try:
            with engine.connect() as conn:
                result = conn.execute(text(query), {'user_id': user_id})
                books = [f"{row['title']} by {row['authors']}" for row in result.mappings()]

            if not books:
                resp.status = falcon.HTTP_200
                resp.media = {'recommendations': [], 'message': 'No books in reading list to base recommendations on.'}
                return

            # Step 2: Build simple prompt for AI - ask for list only, no explanations
            prompt = (
                "Here is a list of books I plan to read:\n"
                + "\n".join(f"- {book}" for book in books)
                + "\n\nPlease recommend 5 other book titles and their authors only, no explanations. "
                  "Return them as a simple numbered list, like:\n"
                  "1. Title by Author\n2. Title by Author\n..."
            )

            # Step 3: Call OpenAI API for recommendations
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
                n=1,
                stop=None,
            )

            ai_text = response.choices[0].text.strip()

            # Step 4: Parse AI response into list of (title, author)
            recs = []
            lines = ai_text.split("\n")
            for line in lines:
                # remove numbering if present and extra spaces
                clean_line = re.sub(r"^\d+\.?\s*", "", line).strip()
                if " by " in clean_line:
                    title, author = clean_line.split(" by ", 1)
                    recs.append({'title': title.strip(), 'author': author.strip()})

            # Step 5: For each recommended book, fetch thumbnail from Google Books API
            for book in recs:
                params = {
                    'q': f"intitle:{book['title']}+inauthor:{book['author']}",
                    'maxResults': 1,
                }
                gb_response = requests.get(GOOGLE_BOOKS_API, params=params)
                if gb_response.status_code == 200:
                    data = gb_response.json()
                    if 'items' in data and len(data['items']) > 0:
                        volume_info = data['items'][0].get('volumeInfo', {})
                        image_links = volume_info.get('imageLinks', {})
                        thumbnail = image_links.get('thumbnail')
                        book['thumbnail'] = thumbnail
                    else:
                        book['thumbnail'] = None
                else:
                    book['thumbnail'] = None

            # Step 6: Return recommendations JSON
            resp.status = falcon.HTTP_200
            resp.media = {'recommendations': recs}

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Failed to fetch recommendations', 'details': str(e)}
