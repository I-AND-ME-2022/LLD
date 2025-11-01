
from Parking.parking_spot import ParkingSpot
from Parking.spot_type import SpotType

class CarParkingSpot(ParkingSpot):
    
    def __init__(self,fee:float):
        super().__init__(SpotType.FOUR_WHEELER,fee)
    