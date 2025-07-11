# from db.connection import engine
# from db.base import Base
# import models.user_model
# import models.book_model

from backend.db.connection import engine
from backend.db.base import Base
import backend.models.user_model
import backend.models.book_model


def create_tables():
    Base.metadata.create_all(engine)
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()
