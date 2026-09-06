# PROGRAMMED BY: ROXANNE-MAE B. RABIMBI

from customerManagement import CustomerManagement
from menuManagement import MenuManagement


class OrderProcessing:
    def __init__(self, customerManagement, menuManagement):
        self.customerManagement = customerManagement
        self.menuManagement = menuManagement
        self.cart = self.customerManagement.getCart()

    def _saveCart(self):
        self.customerManagement.setCart(self.cart)

    def showCart(self):
        print("\n<===== Your Cart =====>")

        if not self.cart:
            print("Your cart is empty.")
            return

        total = 0

        for itemId, quantity in self.cart.items():
            item = self.menuManagement.getItem(itemId)

            if item:
                subtotal = item["price"] * quantity
                total += subtotal
                print(
                    f"{itemId}. {item['item']} "
                    f"x{quantity} - ₱{subtotal:.2f}"
                )

        print(f"\nTotal: ₱{total:.2f}")

    def addToCart(self):
        self.menuManagement.displayMenu()

        try:
            itemId = int(input("\nEnter item number: "))
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        if self.menuManagement.getItem(itemId) is None:
            print("Item not found.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        self.cart[itemId] = self.cart.get(itemId, 0) + quantity
        self._saveCart()

        print("Item added to cart.")

    def setQuantity(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        self.showCart()

        try:
            itemId = int(input("\nEnter item number: "))
            quantity = int(input("Enter new quantity: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        if itemId not in self.cart:
            print("Item is not in your cart.")
            return

        if quantity <= 0:
            self.removeFromCart(itemId)
            return

        self.cart[itemId] = quantity
        self._saveCart()
        print("Quantity updated.")

    def removeFromCart(self, itemId=None):
        if not self.cart:
            print("Your cart is empty.")
            return

        if itemId is None:
            self.showCart()

            try:
                itemId = int(input("\nEnter item number to remove: "))
            except ValueError:
                print("Please enter a valid number.")
                return

        if itemId not in self.cart:
            print("Item is not in your cart.")
            return

        del self.cart[itemId]
        self._saveCart()
        print("Item removed from cart.")

    def getTotal(self):
        total = 0

        for itemId, quantity in self.cart.items():
            item = self.menuManagement.getItem(itemId)

            if item:
                total += item["price"] * quantity

        return total

    def proceedToCheckout(self):
        if not self.cart:
            print("Your cart is empty.")
            return False

        self.showCart()
        return True

    def processOrder(self):
        while True:
            print("\n<===== Process Your Order =====>")
            print("[1] Show Cart")
            print("[2] Add Item")
            print("[3] Set Quantity")
            print("[4] Remove Item")
            print("[5] Proceed to Payment")
            print("[6] Exit")

            try:
                option = int(input("Select an option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if option == 1:
                self.showCart()
            elif option == 2:
                self.addToCart()
            elif option == 3:
                self.setQuantity()
            elif option == 4:
                self.removeFromCart()
            elif option == 5:
                return self.proceedToCheckout()
            elif option == 6:
                return False
            else:
                print("Invalid option.")
