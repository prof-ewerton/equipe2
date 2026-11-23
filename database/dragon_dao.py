import sqlite3

class DAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor =  connection.cursor()
        
    def create(self, lore: str, idade: int, voa: bool, tipo: str):
        try:
            self.cursor.execute("INSERT INTO dragons (lore, idade, voa, tipo) VALUES (?, ?, ?, ?)", (lore, idade, voa, tipo))
            self.connection.commit()
            print("Inserção realizada com sucesso.")
        except sqlite3.Error as erro:
            print("Erro ao realizar operação.")
    
    
    def list(self):
        try:
            self.cursor.execute("SELECT * FROM dragons")
            self.connection.commit()
            print("Leitura realizada com sucesso.")
            
        except sqlite3.Error as erro:
            print("Erro ao ler tabela.")