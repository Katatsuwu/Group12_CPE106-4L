# PROGRAMMED BY: SANTI GABRIEL C. DE LEON

from customerManagement import CustomerManagement
from orderProcessing import OrderProcessing


class PaymentAndDelivery:

    def __init__(self, customerManagement=None, orderProcessing=None):
        self.customerManagement = customerManagement
        self.orderProcessing = orderProcessing

    def confirmAddress(self):
        pass

    def changeAddress(self):
        pass

    def confirmOrder(self):
        pass
