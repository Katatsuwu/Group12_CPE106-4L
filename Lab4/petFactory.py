class petFactory():
    def __init__(self):
        self.pets = []

    def create_pet(self, pet_type, name):
        if pet_type == "dog":
            pet = Dog(name)
        elif pet_type == "cat":
            pet = Cat(name)
        else:
            raise ValueError("Unknown pet type")
        self.pets.append(pet)
        return pet