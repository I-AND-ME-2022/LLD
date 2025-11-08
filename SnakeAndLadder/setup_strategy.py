
from abc import ABC, abstractmethod

from board_entity import Ladder, Snake


class BoardSetUpStrategy(ABC):
    
    @abstractmethod
    def setup_board(self,board):
        pass

class StandardSetUp(BoardSetUpStrategy):
    
    def setup_board(self, board):
        
        board.add_entity(Snake(5,1),1)
        board.add_entity(Ladder(5,80),5)
    
        