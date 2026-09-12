    class PetOwner:
    def __init__(self, owner_id, name, contact_number):
        self.__owner_id = owner_id
        self.__name = name
        self.__contact_number = contact_number

    # Getters
    def get_owner_id(self):
        return self.__owner_id

    def get_name(self):
        return self.__name

    def get_contact_number(self):
        return self.__contact_number

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def display_info(self):
        return (
            f"Owner ID: {self.__owner_id}\n"
            f"Name: {self.__name}\n"
            f"Contact Number: {self.__contact_number}"
        )