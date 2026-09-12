import csv
import os


class ClinicDatabase:
    """Singleton database for all clinic records, with CSV persistence."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.owners = []
        self.pets = []
        self.appointments = []
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.load_data()
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def _csv_path(self, filename):
        return os.path.join(self.base_dir, filename)

    def load_data(self):
        # Imports are kept local so the database remains compatible with
        # the existing project files.
        from petOwner import PetOwner
        from petManagement import Pet

        self.owners = []
        self.pets = []
        self.appointments = []

        owner_path = self._csv_path("owners.csv")
        if os.path.exists(owner_path):
            with open(owner_path, newline="", encoding="utf-8") as file:
                for row in csv.DictReader(file):
                    self.owners.append(
                        PetOwner(row["owner_id"], row["name"], row["contact_number"])
                    )

        pet_path = self._csv_path("pets.csv")
        if os.path.exists(pet_path):
            with open(pet_path, newline="", encoding="utf-8") as file:
                for row in csv.DictReader(file):
                    owner = self.find_owner(row["owner_id"])
                    self.pets.append(
                        Pet(row["pet_id"], row["name"], row["pet_type"], row["owner_id"], owner)
                    )

        appointment_path = self._csv_path("appointments.csv")
        if os.path.exists(appointment_path):
            from appointmentManagement import Appointment
            with open(appointment_path, newline="", encoding="utf-8") as file:
                for row in csv.DictReader(file):
                    appointment = Appointment(
                        row["appointment_id"],
                        row["owner_id"],
                        row["pet_name"],
                        row["date"],
                        row["time"],
                    )
                    appointment.set_status(row["status"])
                    self.appointments.append(appointment)

    def save_data(self):
        with open(self._csv_path("owners.csv"), "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["owner_id", "name", "contact_number"])
            writer.writeheader()
            for owner in self.owners:
                writer.writerow({
                    "owner_id": owner.get_owner_id(),
                    "name": owner.get_name(),
                    "contact_number": owner.get_contact_number(),
                })

        with open(self._csv_path("pets.csv"), "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["pet_id", "name", "pet_type", "owner_id"]
            )
            writer.writeheader()
            for pet in self.pets:
                writer.writerow({
                    "pet_id": pet.get_pet_id(),
                    "name": pet.get_name(),
                    "pet_type": pet.get_pet_type(),
                    "owner_id": pet.get_owner_id(),
                })

        with open(
            self._csv_path("appointments.csv"), "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "appointment_id", "owner_id", "pet_name",
                    "date", "time", "status"
                ],
            )
            writer.writeheader()
            for appointment in self.appointments:
                writer.writerow({
                    "appointment_id": appointment.get_appointment_id(),
                    "owner_id": appointment.get_owner_id(),
                    "pet_name": appointment.get_pet_name(),
                    "date": appointment.get_date(),
                    "time": appointment.get_time(),
                    "status": appointment.get_status(),
                })

    def find_owner(self, owner_id):
        for owner in self.owners:
            if owner.get_owner_id() == owner_id:
                return owner
        return None

    def find_pet(self, pet_id):
        for pet in self.pets:
            if pet.get_pet_id() == pet_id:
                return pet
        return None

    def find_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.get_appointment_id() == appointment_id:
                return appointment
        return None

    def add_owner(self, owner):
        self.owners.append(owner)
        self.save_data()

    def add_pet(self, pet):
        self.pets.append(pet)
        self.save_data()

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        self.save_data()

    def clear_all(self):
        self.owners.clear()
        self.pets.clear()
        self.appointments.clear()
        self.save_data()
