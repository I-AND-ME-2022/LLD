


from Payment.payment import PaymentStrategy


class CardPayment(PaymentStrategy):
    
    def pay_bill(self,amount:float):
        print(f"{amount} paid via card !")
    