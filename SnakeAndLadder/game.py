from collections import deque
from board import Board
from dice import Dice
from player import Player
from rule_strategy import RuleStrategy
from setup_strategy import BoardSetUpStrategy


class SnakeAndLadderGame:
    
    def __init__(self,board:Board,dice:Dice,rule:RuleStrategy):
        self.board = board
        self.dice = dice
        self.rule = rule
        self.players :deque[Player] = deque([])
        self.is_game_over = False
    
    def add_player(self,player:Player):
        self.players.append(player)

    def play(self):
        if len(self.players) < 2:
            return "Minimum Two Players required to play the Game !!"
        print("Game Start !")
        while not self.is_game_over:
            player = self.players.popleft()
            print(f"{player.get_name()} is playing game !!!")
            player_pos = player.get_pos()
            print(f"{player.get_name()} is at {player.get_pos()} position")
            print("*******************************************************")
            dice_val = self.dice.roll()
            new_pos = self.rule.calculate_new_pos(player_pos,dice_val,self.board)
            if self.rule.is_valid_move(new_pos,self.board):
                
                if self.rule.has_winner(new_pos,self.board):
                    print(f"{player.get_name()} is a winner !!!")
                    print(f"game over !")
                    self.is_game_over = True
                    return
            else:
                print(f"you exactly need {self.board.get_size() -player_pos} value !!!")
            self.players.append(player)
                        
    
    def set_up_board(self,board_setup_strategy:BoardSetUpStrategy):
        board_setup_strategy.setup_board(self.board)
