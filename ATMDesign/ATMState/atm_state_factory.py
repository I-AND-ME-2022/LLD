
from ATMState.state import State
from ATMState.dispence_cash_state import DispenceCashState
from ATMState.eject_card_state import EjectCardState
from ATMState.has_card_state import HasCardState
from ATMState.idle_state import IdleState
from ATMState.select_operation_state import SelectOperationState
from ATMState.withdraw_state import WithDrawState


class AtmStateFactory:
    
    @staticmethod
    def create_atm_state(state_type):
        state = None
        match state_type:
            
            case State.IdleState:
                state =  IdleState()
            case State.HasCardState:
                state = HasCardState()
            case State.SelectOperationState:
                state = SelectOperationState()
            case State.WithDrawState:
                state = WithDrawState()
            case State.DispenceCashState:
                state = DispenceCashState()
            case State.EjectCardState:
                state = EjectCardState()
                
        return state