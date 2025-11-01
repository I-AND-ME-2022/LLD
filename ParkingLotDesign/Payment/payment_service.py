

from Payment.card_payment import CardPayment
from Payment.upi_payment import UPIPayment


class PaymentService:
    
    def payment(amount):
        
        payement = None
        print("select the payment method")
        print("1. Card Payment\n 2. UPI Payment")
        option = int(input("Enter option: "))
        
        match option:
            
            case 1:
                payement = CardPayment()
            case 2:
                payement = UPIPayment()
            case _:
                print("Invalid option !")
        payement.pay_bill(amount)