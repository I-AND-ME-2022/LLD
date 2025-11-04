class Card:
    
    def __init__(self,card_num,pin,account_num):
        self.pin = pin
        self.card_num = card_num
        self.account_num = account_num
    
    def validate_pin(self,pin):
        return self.pin == pin
    
        