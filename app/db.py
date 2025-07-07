import mysql.connector
import sys
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    
    def __init__(self):
        self.connection = mysql.connector.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=3306,
                database="test_db"
        )

    def __enter__(self):
        self.cursor = self.connection.cursor(dictionary=True)
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        self.connection.close()
