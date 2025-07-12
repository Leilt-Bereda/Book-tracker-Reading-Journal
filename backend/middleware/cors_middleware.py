# cors_middleware.py
import falcon

class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        resp.set_header('Access-Control-Allow-Headers', 'Authorization, Content-Type')
        if req.method == 'OPTIONS':
            resp.status = falcon.HTTP_200
            # Return immediately to handle preflight OPTIONS requests
            return
