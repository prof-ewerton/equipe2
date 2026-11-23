class cavaleiroDao:
    def create(self, ususario):
        connection = get_conneciton()
        
        try:
            cursor = connection.execute("""
                insert into cavaleiro (nome, nivel, possuiDragao, classe)
                values (?,?,?,?)
            """)
            connection.commit()
            return cursor.lastrowid()
        finally:
            connection.close()
            
    def list(self):
        connection = get_connection()
        
        try:
            cursor = connection.execute("""
                select nome, nivel, possuiDragao, calsse, fromm cavaleiro
            """)
            connection.fetchall()
            return cursor.lastrowid()
        finally:
            connection.close()
            
    def get(self, id_cavaleiro):
        connection = get_connection()
        
        try:
            cursor = connection.execute("""
                select nome, nivel, possuiDragao, calsse,
                from cavaleiro where id = ?
            """)
            connection.fetchall()
            return cursor.lastrowid()
        finally:
            connection.close()
        