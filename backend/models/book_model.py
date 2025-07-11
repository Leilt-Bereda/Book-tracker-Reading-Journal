# CONNECTS THE USER AND BOOKS, ADDING UPDATING STATUS PROGRESS NOTES
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum
import datetime
from backend.db.base import Base
  # import shared Base

class ReadingStatus(enum.Enum):
    NOT_STARTED = "not started"
    READING = "reading"
    FINISHED = "finished"

# Represents the book metadata
# Stores public book info
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    google_book_id = Column(String(100), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    authors = Column(Text)
    description = Column(Text)
    published_date = Column(String(20))
    thumbnail_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user_books = relationship("UserBook", back_populates="book")

#Tracks a specific user's relationship with a book
class UserBook(Base):
    __tablename__ = 'user_books'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    status = Column(Enum(ReadingStatus), default=ReadingStatus.NOT_STARTED)
    progress = Column(Integer, default=0)
    rating = Column(Integer)
    notes = Column(Text)
    added_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="user_books")
    book = relationship("Book", back_populates="user_books")
