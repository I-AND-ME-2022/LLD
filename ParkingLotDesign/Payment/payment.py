from abc import ABC,abstractmethod

class PaymentStrategy(ABC):
    
    @abstractmethod
    def pay_bill(amount:float):
        pass