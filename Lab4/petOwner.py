# By: Roxanne-Mae B. Rabimbi

class PetOwner:

    def __init__(self, owner_id, name, contact_number):
        self.__owner_id = owner_id
        self.__name = name
        self.__contact_number = contact_number

    # Get Owner ID
    def get_owner_id(self):
        return self.__owner_id

    # Get Name
    def get_name(self):
        return self.__name

    # Get Contact Number
    def get_contact_number(self):
        return self.__contact_number

    # Update Name
    def set_name(self, name):
        self.__name = name

    # Update Contact Number
    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    # Display Owner Information
    def display_info(self):
        print("\n===== PET OWNER INFORMATION =====")
        print(f"Owner ID: {self.__owner_id}")
        print(f"Name: {self.__name}")
        print(f"Contact Number: {self.__contact_number}")