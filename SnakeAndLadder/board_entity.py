from abc import ABC
from uuid import uuid4


class BoardEntity(ABC):
    
    def __init__(self, name : str, start_pos: int, end_pos: int):
        self.id = uuid4
        self.name = name
        self.start_pos = start_pos
        self.end_pos = end_pos
    
    def get_name(self):
        return self.name

    def get_start_pos(self):
        return self.start_pos
    
    def get_end_pos(self):
        return self.end_pos

class Snake(BoardEntity):
    
    def __init__(self, start_pos, end_pos):
        super().__init__("Snake", start_pos, end_pos)

class Ladder(BoardEntity):
    
    def __init__(self, start_pos, end_pos):
        super().__init__("Ladder", start_pos, end_pos)
        
        