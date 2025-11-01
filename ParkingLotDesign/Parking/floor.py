from collections import defaultdict
from typing import Dict, List
from uuid import uuid4

from Parking.parking_spot import ParkingSpot
from vehicle.vehicle import Vehicle

class Floor:
    
    def __init__(self):
        self.id: str = uuid4()
        self.parking_spots: Dict[str,List[ParkingSpot]]=defaultdict(list)
    
    def get_spot(self,vehicle:Vehicle,spot_id):
        
        for spot in self.parking_spots[vehicle.vehicle_type.value]:
            if str(spot.id)==spot_id and spot.can_park_vehicle():
                spot.park_vehicle(vehicle.license_num)
                print(f"parked the vehilce at floor {self.id} on the {spot.id} spot !!")
                return spot
        
        return False

    def vacate_spot(self,vehicle:Vehicle,spot_id):
        
        for spot in self.parking_spots[vehicle.vehicle_type.value]:
            
            if str(spot.id) == spot_id and spot.can_unpark_vehicle(vehicle.license_num):
                print(f"unparked the vehicle from floor {self.id}!!")
                return True
        return False
    
    def add_spot(self,Spot:ParkingSpot):
        
        self.parking_spots[Spot.spot_type.value].append(Spot)
        
    def remove_spot(self,Spot:ParkingSpot):
        self.parking_spots[Spot.spot_type.value].remove(Spot)
    
    def display(self,vehicle_type):
        print("spots:...................................")
        for spot in self.parking_spots[vehicle_type.value]:
            
            print(spot.id)
        
        
                
    