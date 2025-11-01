from uuid import uuid4
from abc import ABC


class ParkingSpot(ABC):
    
    def __init__(self,spot_type:str,fee:float):
        self.id:str= uuid4()
        self.spot_type:str= spot_type
        self.fee:float=fee
        self.is_avalible:bool=True
        self.parked_vehicle_id: str= None
    
    def get_spot_type(self):
        return self.spot_type
    
    def get_fee(self):
        return self.fee
    def set_fee(self,fee):
        
        self.fee = fee
    
    def park_vehicle(self,id):
        self.parked_vehicle_id = id
        self.is_avalible = False
    
    def unparck_vehicle(self):
        self.parked_vehicle_id = None
        self.is_avalible = True
    
    def can_park_vehicle(self):
        return self.is_avalible
    
    def can_unpark_vehicle(self,vehicle_id):
        return self.parked_vehicle_id == vehicle_id
    