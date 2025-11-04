from abc import ABC, abstractmethod
class Dispencer(ABC):
    
    
    @abstractmethod
    def dispence(self,amount:int):
        pass
    
    @abstractmethod
    def can_dispence(self,amount:int):
        pass
    
    @abstractmethod
    def set_next_dispencer(self,dispencer):
        pass

   