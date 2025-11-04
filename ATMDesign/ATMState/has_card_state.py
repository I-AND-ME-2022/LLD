

from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card



class HasCardState(AtmState):
    
    def insert_card(self,atm,card:Card):
        print("card already insereted")
    
    def select_operation(self,atm):
        print("plz enter the pin before transaction")
    
    def enter_pin(self,atm):
        pin = input("enter pin: ")
        from ATMState.atm_state_factory import AtmStateFactory
        if atm.bank.validate_card_pin(atm.inserted_card,pin):
            atm.set_state(AtmStateFactory.create_atm_state(State.SelectOperationState))
            atm.select_operation()
        else:
            print("Invalid pin or Card !!!")
            atm.set_state(AtmStateFactory.create_atm_state(State.EjectCardState))
            atm.eject_card()
            
    
    def enter_amount(self,atm):
        print("plz enter the pin")
    
    def dispence_cash(self,atm):
        print("plz enter the pin")
    
    def eject_card(self,atm):
        print("plz enter the pin")
    
    
    