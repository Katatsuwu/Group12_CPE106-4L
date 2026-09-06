# PROGRAMMED BY: SEAN PATRICK A. RELUCIO


class MenuManagement:
    menu = {
        1: {
            "item": "Tatang's Chicken Rice Meal",
            "price": 120.00,
            "desc": "Straight fresh out of a cockfighting arena, rushed straight to the plate while still pumped on pure adrenaline."
        },
        2: {
            "item": "Borger ka saken",
            "price": 150.00,
            "desc": "Beef patty with lettuce, tomato, cheese, and made with love."
        },
        3: {
            "item": "Chicken Wings na Naka-Jetski",
            "price": 180.00,
            "desc": "Crispy wings so fast they flew straight into your plate."
        },
        4: {
            "item": "Friend's Fries",
            "price": 80.00,
            "desc": "Crispy golden french fries that was never truly yours."
        },
        5: {
            "item": "Iced Tea ala Marites",
            "price": 60.00,
            "desc": "Hey sis what's the tea? ICED TEA! Brewed fresh with neighborhood chika and high-grade neighborhood gossip."
        },
        6: {
            "item": "Coke Missmo?",
            "price": 50.00,
            "desc": "Chilled carbonated soft drink that will make you feel cold out of your longing for the person that will no longer return."
        }
    }

    def displayMenu(self):
        print("\n<===== Tom's Best Cuisine Menu =====>")

        for itemId, item in self.menu.items():
            print(
                f"{itemId}. {item['item']} - "
                f"₱{item['price']:.2f}"
            )

    def viewItemDetails(self):
        self.displayMenu()

        try:
            itemId = int(input("\nEnter item number: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        item = self.menu.get(itemId)

        if item is None:
            print("Item not found.")
            return

        print(f"\n<===== {item['item']} =====>")
        print(f"Price: ₱{item['price']:.2f}")
        print(f"Description: {item['desc']}")

    def getItem(self, itemId):
        return self.menu.get(itemId)
