# PROGRAMMED BY: SANTI GABRIEL C. DE LEON

from abc import ABC, abstractmethod
from datetime import datetime

from customerManagement import CustomerManagement
from orderProcessing import OrderProcessing


class Payment(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass


class CashPayment(Payment):
    def processPayment(self, amount):
        print(f"Cash payment: ₱{amount:.2f}")
        return True


class CardPayment(Payment):
    def processPayment(self, amount):
        print(f"Card payment: ₱{amount:.2f}")
        print("Card payment approved.")
        return True


class EWalletPayment(Payment):
    def processPayment(self, amount):
        print(f"E-Wallet payment: ₱{amount:.2f}")
        print("E-Wallet payment approved.")
        return True


class PaymentAndDelivery:
    def __init__(self, customerManagement, orderProcessing):
        self.customerManagement = customerManagement
        self.orderProcessing = orderProcessing

    def accessCart(self):
        self.orderProcessing.showCart()

    def getTotalPrice(self):
        return self.orderProcessing.getTotal()

    def confirmAddress(self):
        customer = self.customerManagement.currentCustomer

        print(
            f"\nCurrent delivery address: "
            f"{customer.deliveryAddress}"
        )

        choice = input("Use this address? [Y/N]: ").strip().lower()

        if choice == "y":
            return True

        if choice == "n":
            return self.changeAddress()

        print("Invalid choice.")
        return False

    def changeAddress(self):
        newAddress = input("Enter new delivery address: ").strip()

        if not newAddress:
            print("Address cannot be empty.")
            return False

        self.customerManagement.setDelvAdd(newAddress)
        self.customerManagement.save()

        print("Delivery address updated.")
        return True

    def selectPaymentMethod(self, amount):
        print("\n<===== Payment Method =====>")
        print("[1] Cash")
        print("[2] Card")
        print("[3] E-Wallet")

        try:
            choice = int(input("Select payment method: "))
        except ValueError:
            print("Please enter a valid number.")
            return False

        if choice == 1:
            payment = CashPayment()
        elif choice == 2:
            payment = CardPayment()
        elif choice == 3:
            payment = EWalletPayment()
        else:
            print("Invalid payment method.")
            return False

        return payment.processPayment(amount)

    def confirmOrder(self):
        if not self.orderProcessing.cart:
            print("Your cart is empty.")
            return False

        self.accessCart()

        if not self.confirmAddress():
            print("Order cancelled.")
            return False

        total = self.getTotalPrice()

        if not self.selectPaymentMethod(total):
            print("Payment failed.")
            return False

        orderId = "ORD-" + datetime.now().strftime("%Y%m%d%H%M%S")

        self.customerManagement.addOrder(orderId)

        self.orderProcessing.cart.clear()
        self.customerManagement.setCart({})

        print(f"\nOrder {orderId} confirmed.")
        print("Payment successful.")
        print("Delivery status: Completed")

        return True

    def viewCompletedTransactions(self):
        print("\n<===== Completed Transactions =====>")

        orders = self.customerManagement.getOrders()

        if not orders:
            print("No transactions found.")
            return

        for orderId in orders:
            print(f"- {orderId}")
