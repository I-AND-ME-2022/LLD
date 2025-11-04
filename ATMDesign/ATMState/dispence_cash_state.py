from ATMState.atm_state import AtmState

from ATMState.state import State
from BankService.card import Card


class DispenceCashState(AtmState):
    
    def insert_card(self,atm,card:Card):
        print("cash is dispencing plz wait...")
    
    def select_operation(self,atm):
        print("cash is dispencing plz wait...")
    
    def enter_pin(self,atm):
        print("cash is dispencing plz wait...")
    
    def enter_amount(self,atm):
        print("cash is dispencing plz wait...")
    
    def dispence_cash(self,atm):
        from ATMState.atm_state_factory import AtmStateFactory
        if atm.can_withdraw(atm.entered_amount):
            if atm.bank.can_withdraw(atm.entered_amount,atm.inserted_card):
                if atm.deduct(atm.entered_amount) and atm.bank.withdraw(atm.entered_amount,atm.inserted_card):                    
                    print("plz collect your cash!!")
                else:
                    print("Transaction Failed")
            else:
                print("insufficient balance in your account !!!")
            
        else:
            print("insufficient amount in atm !!")
        atm.set_state(AtmStateFactory.create_atm_state(State.EjectCardState))
        atm.eject_card()
    def eject_card(self,atm):
        print("cash is dispencing plz wait...")
    