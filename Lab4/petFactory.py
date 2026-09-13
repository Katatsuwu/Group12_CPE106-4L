# By: Emmanuel Gabriel M. Visto

from petManagement import Pet


class PetFactory:
    """Factory for creating supported pet types."""

    SUPPORTED_TYPES = ("dog", "cat", "bird", "rabbit")

    @staticmethod
    def create_pet(pet_id, name, pet_type, owner_id, owner=None):
        pet_type = pet_type.strip().lower()

        if pet_type not in PetFactory.SUPPORTED_TYPES:
            raise ValueError("Unknown pet type")

        return Pet(pet_id, name, pet_type.capitalize(), owner_id, owner)
