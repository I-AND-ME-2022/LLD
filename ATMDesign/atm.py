
from ATMState.atm_state import AtmState
from ATMState.idle_state import IdleState
from BankService.bank import Bank
from BankService.card import Card


class ATM:
    
    def __init__(self,id,bank,cash_dispencer):
        self.id = id
        self.bank: Bank = bank
        self.current_state = IdleState()    
        self.cash_dispencer = cash_dispencer
        self.entered_amount = 0
        self.inserted_card = None
        
    
    def add_cash(self,amount):
        self.balance += amount
    
    def set_state(self,state:AtmState):
        self.current_state = state
    
    def set_amount(self,amount):
        self.entered_amount = amount
    
    def deduct(self,amount):
        if self.can_withdraw(amount):
            self.cash_dispencer.dispence(amount)
            return True
        return False

    def can_withdraw(self,amount):
        return self.cash_dispencer.can_dispence(amount)

    def set_card(self,card:Card):
        self.inserted_card = card
    
    def insert_card(self,card:Card):
        self.current_state.insert_card(self,card)
    
    def enter_pin(self):
        self.current_state.enter_pin(self)
    
    def enter_amount(self):
        self.current_state.enter_amount(self)
        
    def select_operation(self):
        self.current_state.select_operation(self)    
    
    def dispence_cash(self):
        self.current_state.dispence_cash(self)
    
    def eject_card(self):
        self.current_state.eject_card(self)
    
    def reset(self):
        self.entered_amount = 0
        self.inserted_card = None
        
        
    
        
        