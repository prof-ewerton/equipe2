import sqlite3
import get_db_connection from database.connection

def instalar():
    connection = get_db_connection()
        
    try:
        connection.execute("""
        DELETE TABLE IF EXISTS dragons
        CREATE TABLE IF NOT EXISTS dragons
            
        """)