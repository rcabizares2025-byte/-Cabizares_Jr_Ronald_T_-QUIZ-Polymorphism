class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Processing a credit card payment of ${amount:.2f}")


class DigitalWallet(PaymentMethod):
    def __init__(self):
        self.balance = 50.00

    def pay(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Routing ${amount:.2f} through digital wallet")
            print(f"Remaining Balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds in digital wallet.")


def process_checkout(payment_method, amount):
    payment_method.pay(amount)


print("===== PAYMENT GATEWAY =====")
print("1. Credit Card")
print("2. Digital Wallet")

choice = input("How would you like to pay? ")

amount = float(input("Enter payment amount: $"))

if choice == "1":
    payment = CreditCard()
elif choice == "2":
    payment = DigitalWallet()
else:
    print("Invalid payment method.")
    exit()

print("\n===== RECEIPT =====")
process_checkout(payment, amount)