import unittest

from clinicDatabase import ClinicDatabase
from petOwner import PetOwner
from petFactory import PetFactory
from appointmentManagement import Appointment


class ClinicTests(unittest.TestCase):

    def setUp(self):
        self.db = ClinicDatabase.get_instance()
        self.db.clear_all()

    def test_register_pet_owner(self):
        owner = PetOwner("O001", "Juan Dela Cruz", "09123456789")
        self.db.add_owner(owner)

        self.assertIsNotNone(self.db.find_owner("O001"))
        self.assertEqual(self.db.find_owner("O001").get_name(), "Juan Dela Cruz")

    def test_add_pet_record(self):
        owner = PetOwner("O001", "Juan Dela Cruz", "09123456789")
        self.db.add_owner(owner)

        pet = PetFactory.create_pet("P001", "Bruno", "Dog", "O001", owner)
        self.db.add_pet(pet)

        self.assertIsNotNone(self.db.find_pet("P001"))
        self.assertEqual(self.db.find_pet("P001").get_pet_type(), "Dog")

    def test_schedule_appointment(self):
        appointment = Appointment("A001", "O001", "Bruno", "2026-09-15", "10:00 AM")
        self.db.add_appointment(appointment)

        self.assertIsNotNone(self.db.find_appointment("A001"))
        self.assertEqual(self.db.find_appointment("A001").get_status(), "Scheduled")

    def test_cancel_appointment(self):
        appointment = Appointment("A001", "O001", "Bruno", "2026-09-15", "10:00 AM")
        self.db.add_appointment(appointment)

        appointment.set_status("Cancelled")
        self.db.save_data()

        self.assertEqual(self.db.find_appointment("A001").get_status(), "Cancelled")

    def test_singleton_instance(self):
        db1 = ClinicDatabase.get_instance()
        db2 = ClinicDatabase.get_instance()

        self.assertIs(db1, db2)


if __name__ == "__main__":
    unittest.main()
