from uuid import uuid4


class Player:
    
    def __init__(self,name):
        self.id : str = uuid4
        self.name : str = name
        self.pos : int = 0
    
    def set_pos(self,pos):
        self.pos = pos
    
    def get_pos(self):
        return self.pos
    
    def get_name(self):
        return self.name
    