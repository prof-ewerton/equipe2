from database.dragon_dao import DAO

class Service:
    def __init__(self, dao):
        self.dao = dao
        
    def create(self, dragon):
        self.dao.create(dragon.lore, dragon.idade, dragon.voa, dragon.tipo)
        
    def list(self):
        self.dao.list()