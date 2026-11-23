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
        
        insert into cavaleiro(nome, nivel, possuiDragao, classe) values(
            "thomas", 1, True, "defesa",
            "miguel", 3, True, "ataque",
            "joao", 1, False, "guarda",
            "jose", 2, False, "defesa",
            "flavio", 2, True, "ataque",
            )
        connection.commit()
    finally:
        connection.close()
