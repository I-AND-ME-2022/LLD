



from Dispencer.dispencer import Dispencer


class CashDispencer:
    
    def __init__(self,dispencer:Dispencer):
        self.dispencer = dispencer
    
    def can_dispence(self,amount):
        
        if amount ==0 or amount <0 or amount % 10 != 0:
            return False
        return self.dispencer.can_dispence(amount)
    
    def dispence(self,amount):
        return self.dispencer.dispence(amount)