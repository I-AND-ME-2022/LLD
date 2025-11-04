



from Dispencer.dispencer import Dispencer


class NoteDispencer(Dispencer):
    
    def __init__(self,value,num_of_note):
        self.num_of_note = num_of_note
        self.value = value
        self.next_dispencer = None
    
    def set_next_dispencer(self,dispencer:Dispencer):
        self.next_dispencer = dispencer
    
    def can_dispence(self, amount):
        
        if amount >= self.value:
            deduct = min(amount//self.value,self.num_of_note)
            amount -= self.value * deduct
            
            if amount ==0 or self.next_dispencer.can_dispence(amount):
                print(f"{self.num_of_note} notes of {self.value} Deducted")
                return True
            return False
        return self.next_dispencer.can_dispence(amount)
    
    def dispence(self,amount):
        if amount >= self.value:
            deduct = min(amount//self.value,self.num_of_note)
            self.num_of_note -= deduct
            amount -= self.value * deduct
            
            if amount ==0 or self.next_dispencer.dispence(amount):
                print(f"{deduct} notes of {self.value} Deducted")
                return True
            return False
        return self.next_dispencer.dispence(amount)