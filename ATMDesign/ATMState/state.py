from enum import Enum
class State(Enum):
    
    IdleState = "IdleState"
    HasCardState = "HasCardState"
    SelectOperationState = "SelectOperationState"
    WithDrawState = "WithDrawState"
    DispenceCashState = "DispenseCashState"
    EjectCardState = "EjectCardState"