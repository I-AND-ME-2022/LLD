from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card


class WithDrawState(AtmState):
    
    def insert_card(self,atm,card:Card):
        print("card is already inserted plz enter the amount!")
    
    def select_operation(self,atm):
        print("Operation already selected plz enter the amount!")
    
    def enter_pin(self,atm):
        print("pin is already entered plz enter the amount!")
    
    def enter_amount(self,atm):
        from ATMState.atm_state_factory import AtmStateFactory
        amount = int(input("Enter the amount: "))
        atm.set_amount(amount)
        atm.set_state(AtmStateFactory.create_atm_state(State.DispenceCashState))
        atm.dispence_cash()
           
    def dispence_cash(self,atm):
        
        print("plz enter the amount!")
            
    
    def eject_card(self,atm):
        print("plz enter the amount!")
        
    