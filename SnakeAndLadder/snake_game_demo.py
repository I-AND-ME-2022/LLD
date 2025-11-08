from abc import abstractmethod
from board import Board
from dice import Dice
from game import SnakeAndLadderGame
from player import Player
from rule_strategy import StandardRuleStrategy
from setup_strategy import StandardSetUp


class SnakeLadderGameDemo:
    
    @abstractmethod
    def main():
        p1 = Player("Aarti")
        p2 = Player("Pradip")
        board = Board(3)
        dice = Dice(6)
        rule = StandardRuleStrategy()
        setup_strategy = StandardSetUp()
        
        game = SnakeAndLadderGame(board,dice,rule)
        game.set_up_board(setup_strategy)
        
        for p in (p1,p2):
            game.add_player(p)
        game.play()
        
        
        

SnakeLadderGameDemo.main()