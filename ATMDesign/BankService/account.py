from typing import Dict

from BankService.card import Card


class Account:
    
    def __init__(self,account_num,balance):
        self.account_num = account_num
        self.balance = balance
        self.cards : Dict[str,Card] = {}
    
    def validate_card(self,card:Card):
        return self.cards.get(card.card_num,None)
    
    def withdraw(self,amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            print(f"{amount} deducted from account ending with XXXXXXX{self.account_num[-4:]}")
            return True
        print("insufficient amount !!")
        return False
    
    def can_withdraw(self,amount):
        return self.balance >= amount
    
    def add_card(self,card:Card):
        if not self.cards.get(card.card_num,None):
            self.cards[card.card_num] = card
            print("card added !")
            return True
        print("card already exist !")
        return False
    
    