from database.connection import get_connection


def install():
    connection = get_connection()  
    try:
        cursor = connection.cursor() 
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cavaleiro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nivel integer,
                possuiDragao bool,
                classe text
            )
        """)
        connection.commit()
    finally:
        connection.close()
