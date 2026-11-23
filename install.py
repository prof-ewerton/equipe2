import sqlite3
import get_db_connection from database.connection

def instalar():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Conexão à base de dados realizada com sucesso.")
    except sqlite3.Error as erro:
        print("Erro ao conectar com o banco.")