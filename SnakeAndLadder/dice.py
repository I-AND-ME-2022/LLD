import random
from uuid import uuid4


class Dice:
    
    def __init__(self,num_of_face:int):
        self.id :str = uuid4
        self.num_of_face :int = num_of_face
    
    def roll(self):
        return random.randint(1, self.num_of_face)
        