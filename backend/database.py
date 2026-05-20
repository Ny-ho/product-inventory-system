import os
import mysql.connector
from contextlib import contextmanager

# Read from environment variables (Render), or fallback to local settings if empty
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "inventory_db")
DB_PORT = int(os.getenv("DB_PORT", 3306))

def init_db():
    """Connects using environment variables to initialize."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        cursor.execute(f"USE {DB_NAME}")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(220) NOT NULL,
                category VARCHAR(255),
                price DECIMAL(10, 2) NOT NULL,
                stock INT NOT NULL DEFAULT 0
            )
        """)
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Database init warning: {e}")

init_db()

@contextmanager
def get_db_cursor(commit=False):
    """Provides a safe database connection pooling technique."""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

# import mysql.connector
# from contextlib import contextmanager

# @contextmanager
# def get_db_cursor(commit=False):
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="inventory_db"

#     )
#     cursor=connection.cursor(dictionary=True)
#     yield cursor
#     if commit:
#         connection.commit()
#     cursor.close()
#     connection.close()

# if __name__=="__main__":
#     pass

