# MAIN APPLICATION SETUP, 
# CREATING THE FALCON APP AND 
# CONNECTING ROUTES

import falcon
from middleware.cors_middleware import CORSMiddleware
from routes.auth import RegisterResource, LoginResource
from routes.book_search import BookSearchResource
from routes.books import UserBooksResource
from routes.recommendations import RecommendationsResource

# instantiate resource handlers
register = RegisterResource()
log_in = LoginResource()
book_search = BookSearchResource()
add_books = UserBooksResource()
book_rec = RecommendationsResource()
# create the falon app and map the routes
app = falcon.App()
app = falcon.App(middleware=[CORSMiddleware()])

app.add_route("/auth/register", register)
app.add_route("/auth/login", log_in)
app.add_route("/books/search", book_search)
app.add_route("/user/books", add_books)
app.add_route("/recommendations", book_rec)



class HealthCheckResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = {"message": "API is running"}

app.add_route("/", HealthCheckResource())

if __name__ == '__main__':
    from wsgiref import simple_server
    with simple_server.make_server('localhost', 8000, app) as httpd:
        print("Serving on http://localhost:8000")
        httpd.serve_forever()

