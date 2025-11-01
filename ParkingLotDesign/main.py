
from vehicle.vehicle_type import VehicleType
from parking_lot import ParkingLot
from Parking.car_parking_spot import CarParkingSpot
from Parking.floor import Floor


class main:
    
    @staticmethod
    def run():
        
        # 1 floor 2 spot
        
        floor = Floor()
        for _ in range(2):
            floor.add_spot(CarParkingSpot(50))
        
        parking_lot = ParkingLot()
        parking_lot.floors.append(floor)
        
        vehicle = parking_lot.enter_the_vehicle("74323656",VehicleType.CAR.value)
        spot_id = parking_lot.select_spot(vehicle)
        print(f"{spot_id} is selected !!")
        
        ticket = parking_lot.park_vehicle(vehicle,spot_id)
        parking_lot.unpark_vehicle(vehicle,spot_id,ticket)
main.run()