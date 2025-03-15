from sqlalchemy import create_engine, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def query_database(query: str):
    """Executes a SQL query and returns results."""
    with engine.connect() as connection:
        result = connection.execute(text(query))
        return result.fetchall()
