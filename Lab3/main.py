# LABORATORY ACTIVITY 3 | GROUP 12

from customerManagement import CustomerManagement
from menuManagement import MenuManagement
from orderProcessing import OrderProcessing
from paymentDelivery import PaymentAndDelivery


def customerMenu(customerManagement):
    while True:
        print("\n<===== Customer Management =====>")
        print("[1] View Profile")
        print("[2] Edit Profile")
        print("[3] Save")
        print("[4] Discard Changes")
        print("[5] Return")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            customerManagement.viewProfile()
        elif option == 2:
            customerManagement.editProfile()
        elif option == 3:
            customerManagement.save()
            print("Changes saved.")
        elif option == 4:
            customerManagement.discard()
            print("Changes discarded.")
        elif option == 5:
            break
        else:
            print("Invalid option.")


def menuMenu(menuManagement, orderProcessing, paymentDelivery):
    while True:
        print("\n<===== Menu Management =====>")
        print("[1] Display Menu")
        print("[2] View Item Details")
        print("[3] Proceed to Order")
        print("[4] Return")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            menuManagement.displayMenu()
        elif option == 2:
            menuManagement.viewItemDetails()
        elif option == 3:
            if orderProcessing.processOrder():
                paymentMenu(paymentDelivery)
                return
        elif option == 4:
            break
        else:
            print("Invalid option.")


def paymentMenu(paymentDelivery):
    while True:
        print("\n<===== Payment and Delivery =====>")
        print("[1] Access Cart / View Total")
        print("[2] Confirm / Change Address")
        print("[3] Confirm Order / Process Payment")
        print("[4] View Completed Transactions")
        print("[5] Return")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            paymentDelivery.accessCart()
            print(
                f"Total: "
                f"₱{paymentDelivery.getTotalPrice():.2f}"
            )
        elif option == 2:
            paymentDelivery.confirmAddress()
        elif option == 3:
            paymentDelivery.confirmOrder()
        elif option == 4:
            paymentDelivery.viewCompletedTransactions()
        elif option == 5:
            break
        else:
            print("Invalid option.")


def runSystem():
    customerManagement = CustomerManagement()
    menuManagement = MenuManagement()

    while True:
        print("\n<===== TOM'S BEST CUISINE DELIVERY =====>")
        print("[1] Sign In")
        print("[2] Sign Up")
        print("[3] Exit")

        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            if customerManagement.signIn():
                break
        elif option == 2:
            if customerManagement.signUp():
                break
        elif option == 3:
            print("Thank you for using our system!")
            return
        else:
            print("Invalid option.")

    orderProcessing = OrderProcessing(
        customerManagement,
        menuManagement
    )

    paymentDelivery = PaymentAndDelivery(
        customerManagement,
        orderProcessing
    )

    while customerManagement.currentCustomer is not None:
        print(
            f"\nWelcome, "
            f"{customerManagement.currentCustomer.username}!"
        )
        print("Please select a service:")
        print("[1] Customer Profile")
        print("[2] Menu")
        print("[3] Order Processing")
        print("[4] Payment and Delivery")
        print("[5] Logout")

        try:
            option = int(input("Select a service: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            customerMenu(customerManagement)
        elif option == 2:
            menuMenu(menuManagement, orderProcessing, paymentDelivery)
        elif option == 3:
            orderProcessing.processOrder()
        elif option == 4:
            paymentMenu(paymentDelivery)
        elif option == 5:
            customerManagement.logout()
            print("Logged out successfully.")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    runSystem()
