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
        
        self.cursor = self.connection.cursor(dictionary=True)

    def __enter__(self):
        return self.connection, self.cursor
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        self.connection.close()

