from typing import Dict
from BankService.account import Account
from BankService.card import Card


class Bank:
    
    def __init__(self,bank_id,bank_name):
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.accounts : Dict[str,Account] = {}
    
    def get_account(self,account_num):
        return self.accounts.get(account_num,None)
        
    def add_account(self,account:Account):
        if not self.accounts.get(account.account_num,None):
            self.accounts[account.account_num] = account
            print("Account Added !")
            return True
        print("Account Already Exist !!!")
        return False

    def validate_card_pin(self,card:Card,pin):
        account = self.get_account(card.account_num)
        if account:
            if account.validate_card(card):
                if card.validate_pin(pin):
                    return True
                else:
                    print("Invalid Pin !!")
            else:
                print("Invalid Card")
                return False 
        
        print(f"Only {self.bank_name} cards are accepted!!")
        return False
        
    def withdraw(self,amount,card:Card):
        account = self.get_account(card.account_num)
        if account:
            return account.withdraw(amount)
        print("account not found")
        return False
    
    def can_withdraw(self,amount,card):
        account = self.get_account(card.account_num)
        return account.can_withdraw(amount)
            
            
    
    
    