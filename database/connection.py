import os
import sqlite3

def get_db_connection():
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, "base_dados.db")
    return sqlite3.connect(caminho)