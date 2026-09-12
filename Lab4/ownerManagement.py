from petOwner import PetOwner


class OwnerManagement:

    def __init__(self):
        self.owners = []

    # Register a new pet owner
    def register_owner(self, owner):
        self.owners.append(owner)
        return True

    # View all registered pet owners
    def get_owners(self):
        return self.owners

    # Find an owner using Owner ID
    def find_owner(self, owner_id):
        for owner in self.owners:
            if owner.get_owner_id() == owner_id:
                return owner

        return None

    # Display all registered owners
    def display_owners(self):
        if not self.owners:
            print("No registered pet owners.")
            return

        print("\n===== REGISTERED PET OWNERS =====")

        for owner in self.owners:
            print(owner.display_info())
            print("------------------------------")