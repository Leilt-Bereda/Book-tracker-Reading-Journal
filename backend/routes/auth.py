# DEFINES REGISTER AND LOGIN ROUTES
import falcon
import json 
from pydantic import EmailStr, Field, BaseModel, ValidationError
from utils.hash import hash_password, check_password
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from db.connection import engine
from utils.jwt import create_access_token


class Validate(BaseModel):
    email: EmailStr
    password: str
    name: str

class RegisterResource:
    def on_post(self, req, resp):
        try:
            data = req.media  # Read JSON body
            validated_data = Validate(**data)
        except ValidationError as e:
            errors = [{err['loc'][0]: err['msg']} for err in e.errors()]
            resp.status = falcon.HTTP_400
            resp.media = {'validation_errors': errors}
            return


        name = validated_data.name
        email = validated_data.email
        password = validated_data.password

        hashed_password = hash_password(password)

        # At this point, data is valid and hashed_password is ready for storage
        # You would typically save the user info in the database here

        insert_query = """
        INSERT INTO users (name, email, password_hash)
        VALUES (:name, :email, :password_hash)
        """

        try:
            with engine.begin() as conn:
                conn.execute(text(insert_query), {
                    'name': name,
                    'email': email,
                    'password_hash': hashed_password
                })
            resp.status = falcon.HTTP_201
            resp.content_type = 'application/json'
            resp.media = {'message': 'User registered successfully'}
        except IntegrityError as e:
            resp.status = falcon.HTTP_400
            resp.media = {'error': 'Email already registered'}
class LoginValidate(BaseModel):
    email : EmailStr
    password : str
class LoginResource:
    #Accepts email and password from the user
    def on_post(self, req, resp):
        data = req.media
        try:
            validated_data = LoginValidate(**data)
        except ValidationError as e:
            errors = [{err['loc'][0]: err['msg']} for err in e.errors()]
            resp.status = falcon.HTTP_400
            resp.media = {'validation_errors': errors}
            return
        
        email = validated_data.email
        password = validated_data.password

        query = "SELECT * FROM users WHERE email = :email"
        #connects to the PostgreSQL 
        with engine.connect() as conn:
            result = conn.execute(text(query), {'email': email})
            user = result.fetchone()
        if user is None:
            resp.status = falcon.HTTP_401
            resp.media = {'error': 'Invalid email or password'}
            return
        #extract the hashed password from the database row
        stored_password_hash = user[3]
        if not check_password(password, stored_password_hash):
            resp.status = falcon.HTTP_401
            resp.media = {'error': 'Invalid email or password'}
            return

        access_token = create_access_token({'user_id': user[0], 'email': user[2]})
        resp.status = falcon.HTTP_200
        resp.media = {
            "message": "Login successful!",
            "access_token": access_token
        }
