from abc import ABC, abstractmethod


from BankService.card import Card

class AtmState(ABC):
    
    @abstractmethod
    def insert_card(self,atm,card:Card):
        pass
    
    @abstractmethod
    def select_operation(self,atm):
        pass
    
    @abstractmethod
    def enter_pin(self,atm):
        pass
    
    @abstractmethod
    def enter_amount(self,atm):
        pass
    
    @abstractmethod
    def dispence_cash(self,atm):
        pass
    
    @abstractmethod
    def eject_card(self,atm):
        pass
    
    