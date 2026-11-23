import sqlite3
import get_db_connection from database.connection

def instalar():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Conexão à base de dados realizada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao conectar com o banco.")
        
    try:
        cursor.execute("""
        DELETE TABLE IF EXISTS dragons
        CREATE TABLE IF NOT EXISTS dragons(
        id INTEGER PRIMARY KEY AUTOINCREMET,
        lore TEXT,
        idade INTEGER NOT NULL DEFAULT 0,
        voa BOOLEAN,
        )
        """)
        
        connection.commit()
        print("Tabela criada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao criar tabela.")
    finally:
        print("Conexão encerrada.")
        