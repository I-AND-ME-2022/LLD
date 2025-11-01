from ParkingLot.parking_spot import ParkingSpot
from spot_type import SpotType

class BikeParkingSpot(ParkingSpot):
    
    def __init__(self,fee:float):
        super().__init__(SpotType.TWO_WHEELER,fee)
    