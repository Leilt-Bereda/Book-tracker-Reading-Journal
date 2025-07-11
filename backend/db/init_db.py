from sqlalchemy import create_engine, text

username = 'postgres'
password = '2529gphm'
host = 'localhost'
port = '5432'
database = 'book_tracker'

DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URL)

def create_users_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with engine.connect() as conn:
        conn.execute(text(create_table_query))
        print("Users table created or already exists.")

if __name__ == "__main__":
    create_users_table()
