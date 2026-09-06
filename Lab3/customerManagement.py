# PROGRAMMED BY: EMMANUEL GABRIEL M. VISTO

import csv
import os


class Customer:
    def __init__(self, username, password, phoneNumber="", deliveryAddress=""):
        self.__username = username
        self.__password = password
        self.__phoneNumber = phoneNumber
        self.__deliveryAddress = deliveryAddress

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @property
    def deliveryAddress(self):
        return self.__deliveryAddress

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password

    def setPhoneNum(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def setDelvAdd(self, deliveryAddress):
        self.__deliveryAddress = deliveryAddress


class CustomerManagement:
    fileName = "userData.csv"

    def __init__(self):
        self.currentCustomer = None
        self._ensureFile()

    def _ensureFile(self):
        if not os.path.exists(self.fileName):
            with open(self.fileName, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "username",
                    "password",
                    "phoneNumber",
                    "deliveryAddress",
                    "cart",
                    "orders"
                ])

    def _readUsers(self):
        self._ensureFile()

        with open(self.fileName, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def _writeUsers(self, users):
        fieldNames = [
            "username",
            "password",
            "phoneNumber",
            "deliveryAddress",
            "cart",
            "orders"
        ]

        with open(self.fileName, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerows(users)

    def _findUser(self, username):
        for user in self._readUsers():
            if user["username"] == username:
                return user
        return None

    def signUp(self):
        print("\n<===== Sign Up =====>")

        username = input("Username: ").strip()

        if not username:
            print("Username cannot be empty.")
            return False

        if self._findUser(username):
            print("Username already exists.")
            return False

        password = input("Password: ")
        phoneNumber = input("Phone Number: ").strip()
        deliveryAddress = input("Delivery Address: ").strip()

        self.currentCustomer = Customer(
            username,
            password,
            phoneNumber,
            deliveryAddress
        )

        self.save()
        print("Account created successfully.")
        return True

    def signIn(self):
        print("\n<===== Sign In =====>")

        username = input("Username: ").strip()
        password = input("Password: ")

        user = self._findUser(username)

        if user is None or user["password"] != password:
            print("Invalid username or password.")
            return False

        self.currentCustomer = Customer(
            user["username"],
            user["password"],
            user["phoneNumber"],
            user["deliveryAddress"]
        )

        print(f"Welcome back, {self.currentCustomer.username}!")
        return True

    def viewProfile(self):
        customer = self.currentCustomer

        print("\n<===== My Profile =====>")
        print(f"Username: {customer.username}")
        print(f"Phone Number: {customer.phoneNumber}")
        print(f"Delivery Address: {customer.deliveryAddress}")

    def editProfile(self):
        customer = self.currentCustomer

        print("\n<===== Edit Profile =====>")
        print("Leave an input blank to keep the current value.")

        username = input(
            f"Username [{customer.username}]: "
        ).strip()

        if username and username != customer.username:
            if self._findUser(username):
                print("Username already exists.")
                return
            customer.setUsername(username)

        password = input("Password [hidden]: ")
        phoneNumber = input(
            f"Phone Number [{customer.phoneNumber}]: "
        ).strip()
        deliveryAddress = input(
            f"Delivery Address [{customer.deliveryAddress}]: "
        ).strip()

        if password:
            customer.setPassword(password)

        if phoneNumber:
            customer.setPhoneNum(phoneNumber)

        if deliveryAddress:
            customer.setDelvAdd(deliveryAddress)

        self.save()
        print("Profile updated successfully.")

    def setUsername(self, username):
        self.currentCustomer.setUsername(username)

    def setPassword(self, password):
        self.currentCustomer.setPassword(password)

    def setPhoneNum(self, phoneNumber):
        self.currentCustomer.setPhoneNum(phoneNumber)

    def setDelvAdd(self, deliveryAddress):
        self.currentCustomer.setDelvAdd(deliveryAddress)

    def getCart(self):
        user = self._findUser(self.currentCustomer.username)

        if not user or not user["cart"]:
            return {}

        cart = {}

        for entry in user["cart"].split("|"):
            itemId, quantity = entry.split(":")
            cart[int(itemId)] = int(quantity)

        return cart

    def setCart(self, cart):
        cartData = "|".join(
            f"{itemId}:{quantity}"
            for itemId, quantity in cart.items()
        )

        self._updateUserField("cart", cartData)

    def getOrders(self):
        user = self._findUser(self.currentCustomer.username)

        if not user or not user["orders"]:
            return []

        return user["orders"].split("|")

    def addOrder(self, orderId):
        orders = self.getOrders()
        orders.append(orderId)
        self._updateUserField("orders", "|".join(orders))

    def _updateUserField(self, fieldName, value):
        users = self._readUsers()

        for user in users:
            if user["username"] == self.currentCustomer.username:
                user[fieldName] = value
                break

        self._writeUsers(users)

    def save(self):
        users = self._readUsers()
        customer = self.currentCustomer
        found = False

        for user in users:
            if user["username"] == customer.username:
                user["username"] = customer.username
                user["password"] = customer.password
                user["phoneNumber"] = customer.phoneNumber
                user["deliveryAddress"] = customer.deliveryAddress
                found = True
                break

        if not found:
            users.append({
                "username": customer.username,
                "password": customer.password,
                "phoneNumber": customer.phoneNumber,
                "deliveryAddress": customer.deliveryAddress,
                "cart": "",
                "orders": ""
            })

        self._writeUsers(users)

    def discard(self):
        user = self._findUser(self.currentCustomer.username)

        self.currentCustomer = Customer(
            user["username"],
            user["password"],
            user["phoneNumber"],
            user["deliveryAddress"]
        )

    def logout(self):
        self.currentCustomer = None
