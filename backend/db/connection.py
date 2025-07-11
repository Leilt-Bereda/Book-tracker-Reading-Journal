# MANAGE DATABASE CONNECTIONS
from sqlalchemy import create_engine, text

# Replace these with your actual DB credentials
username = 'postgres'
password = '2529gphm'
host = 'localhost'      # or your remote server IP
port = '5432'           # default PostgreSQL port
database = 'book_tracker'

# Create the connection string
DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the engine
engine = create_engine(DATABASE_URL)

# Test the connection
if __name__ == "__main__":
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Connected to:", result.fetchone()[0])
