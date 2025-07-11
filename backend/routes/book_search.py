# Define endpoint that lets the users search for books by keyword
import falcon
import requests

class BookSearchResource:
    def on_get(self, req, resp):
        query = req.get_param('q')
        if not query:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'Query parameter "q" is required'}
            return

        google_books_api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}'

        try:
            response = requests.get(google_books_api_url)
            response.raise_for_status()
            data = response.json()

            # Optional: simplify the response to send only needed info
            books = []
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                books.append({
                    'id': item.get('id'),
                    'title': volume_info.get('title'),
                    'authors': volume_info.get('authors'),
                    'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail')
                })

            resp.status = falcon.HTTP_200
            resp.media = {'books': books}

        except requests.RequestException as e:
            resp.status = falcon.HTTP_502
            resp.media = {'error': 'Failed to fetch data from Google Books API', 'details': str(e)}

