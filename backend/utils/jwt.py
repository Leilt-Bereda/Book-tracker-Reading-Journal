import jwt
import datetime

SECRET_KEY = 'q@W3rT6yU!zXcV9bn$eFgH7kLmNpO123456'  # Replace with a strong secret, keep this safe!

def create_access_token(data: dict, expires_in_minutes=30):
    payload = data.copy()
    payload.update({
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes),
        'iat': datetime.datetime.utcnow(),
    })
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
