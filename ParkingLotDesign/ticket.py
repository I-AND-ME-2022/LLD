import datetime


class Ticket:
    
    def __init__(self,vehicle_id,spot_id,fee):
        
        self.vehicle_id = vehicle_id
        self.spot_id = spot_id
        self.fee = fee
        self.start_time = datetime.datetime.now()