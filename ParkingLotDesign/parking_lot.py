
import datetime
from math import floor
from typing import List

from vehicle.vehicle import Vehicle
from Payment.payment_service import PaymentService
from vehicle.vehicle_factory import VehicleFactory
from ticket import Ticket

class ParkingLot:
    
    def __init__(self):
        self.floors:List[floor] = []
    def enter_the_vehicle(self,license_num,vehicle_type):
        
        return VehicleFactory.createVehicle(license_num,vehicle_type)
    
    def select_spot(self,vehicle:Vehicle):
        
        for idx,floor in enumerate(self.floors):
            print(f"floor {idx}:......................................")
            floor.display(vehicle.vehicle_type)
        return input("enter the spot id: ")

    def park_vehicle(self,vehicle:Vehicle,spot_id:str):
        
        for floor in self.floors:
            
            spot = floor.get_spot(vehicle,spot_id)
            if spot:
                print("Ticket generated plz collect !")
                return Ticket(vehicle.license_num,spot.id,spot.fee)
        print("invalid spot_id, can't park !")
    
    def unpark_vehicle(self,vehicle:Vehicle,spot_id:str,ticket:Ticket):
        
        for floor in self.floors:
            
            if floor.vacate_spot(vehicle,spot_id):
                self.payment(ticket)
                return
        print("invalid spot_id, can't unpark !")
    
    def payment(self,ticket):
        diff = datetime.datetime.now() - ticket.start_time
        hours = diff.total_seconds() / 3600
        amount = hours * ticket.fee
        PaymentService.payment(amount)
        