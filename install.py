import sqlite3
from database.connection import get_db_connection
from database.dragon_dao import DAO

def instalar():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Conexão à base de dados realizada com sucesso.")
        
    except sqlite3.Error as erro:
        print("Erro ao conectar com o banco.")
        
    try:
        cursor.execute("DROP TABLE IF EXISTS dragons")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dragons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        lore TEXT,
        idade INTEGER NOT NULL DEFAULT 0,
        voa BOOLEAN)
        """)
        
        connection.commit() 

        dao_dragon = DAO(connection)
        dao_dragon.create("aaa", 2000, False, "Gelo")
        print("Tabela criada com sucesso.")
        
    except sqlite3.Error as erro:
        print("Erro ao criar tabela.")
        
    finally:
        connection.close()
        print("Conexão encerrada.")

instalar()