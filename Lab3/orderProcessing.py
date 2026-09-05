# PROGRAMMED BY: ROXANNE-MAE B. RABIMBI

from customerManagement import CustomerManagement
from menuManagement import MenuManagement


class OrderProcessing:

    def __init__(self, customerManagement=None, menuManagement=None):
        self.customerManagement = customerManagement
        self.menuManagement = menuManagement

        # Cart format: {itemId: quantity}
        self.cart = {}

    def showCart(self):
        pass

    def addToCart(self):
        pass

    def setQuantity(self):
        pass

    def removeFromCart(self):
        pass

    def proceedToCheckout(self):
        pass
