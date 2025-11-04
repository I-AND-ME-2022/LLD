from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card



class SelectOperationState(AtmState):
    
    def insert_card(self,atm,card:Card):
        print("......select the operation....")
    
    def select_operation(self,atm):
        from ATMState.atm_state_factory import AtmStateFactory
        print("......select the operation....")
        print("1. Cash Withdraw")
        match int(input()):
            
            case 1:
                atm.set_state(AtmStateFactory.create_atm_state(State.WithDrawState))
                atm.enter_amount()
            case _:
                print("Invalid selection !!")
                atm.set_state(AtmStateFactory.create_atm_state(State.EjectCardState))
                atm.eject_card()
    
    def enter_pin(self,atm):
        print("......select the operation....")
    
    def enter_amount(self,atm):
        print("......select the operation....")
    
    def dispence_cash(self,atm):
        print("......select the operation....")
    
    def eject_card(self,atm):
        print("......select the operation....")