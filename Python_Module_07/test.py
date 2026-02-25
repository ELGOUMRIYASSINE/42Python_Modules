from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using PayPal"


class Checkout:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)


checkout = Checkout(CreditCardPayment())
print(checkout.process_payment(100))

checkout.strategy = PayPalPayment()
print(checkout.process_payment(100))
