from abc import ABC

from board import Board



class RuleStrategy(ABC):
    
    def has_winner(self,pos:int,board:Board):
        pass
    
    def is_valid_move(self,pos:int,board:Board):
        pass
    
    def calculate_new_pos(self,pos:int,dice_value:int,board:Board):
        pass

class StandardRuleStrategy(RuleStrategy):
    
    def has_winner(self,pos:int,board:Board):
        return pos == board.get_size()
        
    
    def is_valid_move(self,pos:int,board:Board):
        return 1<= pos <= board.get_size()
    
    def calculate_new_pos(self,pos:int,dice_value:int,board:Board):
        new_pos = pos + dice_value
        board_entity = board.check_entity(new_pos)
        if board_entity:
            return board_entity.get_end_pos()
        return new_pos
    