#Defines the structure and rules for how the user data is stored
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
import datetime
from backend.db.base import Base
 # import shared Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user_books = relationship("UserBook", back_populates="user")
