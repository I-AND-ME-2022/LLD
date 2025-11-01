from Payment.payment import PaymentStrategy

class UPIPayment(PaymentStrategy):
    
    def pay_bill(self,amount:float):
        print(f"{amount} paid via UPI !")