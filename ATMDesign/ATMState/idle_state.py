
from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card


class IdleState(AtmState):
    
    def insert_card(self,atm,card:Card):
        
        from ATMState.atm_state_factory import AtmStateFactory
        print("card inserted !")
        atm.set_card(card)
        atm.set_state(AtmStateFactory.create_atm_state(State.HasCardState))
        atm.enter_pin()
    
    def select_operation(self,atm):
        print("plz insert the card !!")
    
    def enter_pin(self,atm):
        print("plz insert the card !!")
    
    def enter_amount(self,atm):
        print("plz insert the card !!")
    
    def dispence_cash(self,atm):
        print("plz insert the card !!")
    
    def eject_card(self,atm):
        print("plz insert the card !!")
    
    