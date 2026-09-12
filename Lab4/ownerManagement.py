from petOwner import PetOwner


class OwnerManagement:

    def __init__(self):
        self.owners = []

    # Register a new pet owner
    def register_owner(self, owner):
        self.owners.append(owner)

    # Find an owner using Owner ID
    def find_owner(self, owner_id):
        for owner in self.owners:
            if owner.get_owner_id() == owner_id:
                return owner

        return None

    # Display all registered owners
    def display_owners(self):

        if len(self.owners) == 0:
            print("\nNo registered pet owners.")
            return

        print("\n===== REGISTERED PET OWNERS =====")

        for owner in self.owners:
            print(f"Owner ID: {owner.get_owner_id()}")
            print(f"Name: {owner.get_name()}")
            print(f"Contact Number: {owner.get_contact_number()}")
            print("--------------------------------")


    # Register owner if not already registered
    def register_new_owner(self):

        print("\n===== NEW OWNER REGISTRATION =====")

        owner_id = input("Enter Owner ID: ")

        # Check if owner already exists
        existing_owner = self.find_owner(owner_id)

        if existing_owner is not None:
            print("\nThis owner is already registered.")
            existing_owner.display_info()
            return

        name = input("Enter Owner Name: ")
        contact_number = input("Enter Contact Number: ")

        new_owner = PetOwner(
            owner_id,
            name,
            contact_number
        )

        self.register_owner(new_owner)

        print("\nOwner registered successfully!")
        new_owner.display_info()