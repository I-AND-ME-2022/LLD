from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card


class EjectCardState(AtmState):
    
    def insert_card(self,atm,card:Card):
        print("transaction completed plz wait to collect card")
    
    def select_operation(self,atm):
        print("transaction completed plz wait to collect card")
    
    def enter_pin(self,atm):
        print("transaction completed plz wait to collect card")
    
    def enter_amount(self,atm):
        print("transaction completed plz wait to collect card")
    
    def dispence_cash(self,atm):
        print("transaction completed plz wait to collect card")
    
    def eject_card(self,atm):
        from ATMState.atm_state_factory import AtmStateFactory
        card = atm.inserted_card
        atm.reset()
        print("plz collect your card !!")
        atm.set_state(AtmStateFactory.create_atm_state(State.IdleState))
        return card
    