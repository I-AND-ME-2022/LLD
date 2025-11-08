
from typing import Dict, List
from board_entity import BoardEntity


class Board:
    
    def __init__(self,size):
        self.board_entities : List[BoardEntity] = []
        self.size = size
        self.entity_pos_map : Dict[int,BoardEntity] = {}
    
    def add_entity(self,entity:BoardEntity,pos:int):
        self.board_entities.append(entity)
        self.entity_pos_map[pos] = entity
    
    def check_entity(self,pos):
        return self.entity_pos_map.get(pos,None)

    def can_add_entity(self,pos):
        return not self.entity_pos_map.get(pos,None)
    
    def get_size(self):
        return self.size
    