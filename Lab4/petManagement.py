class Pet:
    def __init__(self, pet_id, name, pet_type, owner_id, owner=None):
        self.__pet_id = pet_id
        self.__name = name
        self.__pet_type = pet_type
        self.__owner_id = owner_id
        self.__owner = owner

    def get_pet_id(self):
        return self.__pet_id

    def get_name(self):
        return self.__name

    def get_pet_type(self):
        return self.__pet_type

    def get_owner_id(self):
        return self.__owner_id

    def get_owner(self):
        return self.__owner

    def display_info(self):
        print("\n===== PET INFORMATION =====")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Name: {self.__name}")
        print(f"Type: {self.__pet_type}")
        print(f"Owner ID: {self.__owner_id}")


class PetManagement:
    """Pet management uses the same ClinicDatabase Singleton."""

    def __init__(self, database=None):
        if database is None:
            from clinicDatabase import ClinicDatabase
            database = ClinicDatabase.get_instance()
        self.database = database

    @property
    def pets(self):
        return self.database.pets

    def add_pet(self, pet):
        if self.database.find_pet(pet.get_pet_id()) is not None:
            return False
        if self.database.find_owner(pet.get_owner_id()) is None:
            return False
        self.database.add_pet(pet)
        return True

    def find_pet(self, pet_id):
        return self.database.find_pet(pet_id)

    def get_pets(self):
        return self.database.pets

    def display_pets(self):
        if not self.pets:
            print("\nNo registered pets.")
            return

        print("\n===== REGISTERED PETS =====")
        for pet in self.pets:
            pet.display_info()
            print("--------------------------------")

