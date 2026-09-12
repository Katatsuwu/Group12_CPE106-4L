from petOwner import PetOwner
from clinicDatabase import ClinicDatabase


class OwnerManagement:

    def __init__(self, database=None):
        self.database = database or ClinicDatabase.get_instance()

    @property
    def owners(self):
        return self.database.owners

    def register_owner(self, owner):
        if self.find_owner(owner.get_owner_id()) is not None:
            return False
        self.database.add_owner(owner)
        return True

    def find_owner(self, owner_id):
        return self.database.find_owner(owner_id)

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

    def register_new_owner(self):
        print("\n===== NEW OWNER REGISTRATION =====")

        owner_id = input("Enter Owner ID: ")
        existing_owner = self.find_owner(owner_id)

        if existing_owner is not None:
            print("\nThis owner is already registered.")
            existing_owner.display_info()
            return

        name = input("Enter Owner Name: ")
        contact_number = input("Enter Contact Number: ")

        new_owner = PetOwner(owner_id, name, contact_number)

        self.register_owner(new_owner)

        print("\nOwner registered successfully!")
        new_owner.display_info()
