from abc import ABC

class Vehicle(ABC):
    
    def __init__(self,license_num:str,vehicle_type:str):
        self.license_num = license_num
        self.vehicle_type = vehicle_type
    
    def get_vehicle_type(self):
        return self.vehicle_type


        
            
        
        
        