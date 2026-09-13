import unittest

from clinicDatabase import ClinicDatabase
from petOwner import PetOwner
from petManagement import PetManagement
from petFactory import PetFactory
from appointmentManagement import Appointment, AppointmentManagement
from ownerManagement import OwnerManagement


class ClinicTests(unittest.TestCase):

    def setUp(self):
        self.db = ClinicDatabase.get_instance()
        self.db.clear_all()
        self.owner_management = OwnerManagement(self.db)
        self.pet_management = PetManagement(self.db)
        self.appointment_management = AppointmentManagement(self.db)

    def tearDown(self):
        self.db.clear_all()

    def test_register_pet_owner(self):
        owner = PetOwner("O001", "Juan Dela Cruz", "09123456789")

        self.assertTrue(self.owner_management.register_owner(owner))
        self.assertIsNotNone(self.owner_management.find_owner("O001"))
        self.assertEqual(
            self.owner_management.find_owner("O001").get_name(),
            "Juan Dela Cruz"
        )

    def test_add_pet_record(self):
        owner = PetOwner("O001", "Juan Dela Cruz", "09123456789")
        self.owner_management.register_owner(owner)

        pet = PetFactory.create_pet("P001", "Bruno", "Dog", "O001", owner)

        self.assertTrue(self.pet_management.add_pet(pet))
        self.assertIsNotNone(self.pet_management.find_pet("P001"))
        self.assertEqual(
            self.pet_management.find_pet("P001").get_pet_type(), "Dog"
        )
        self.assertEqual(
            self.pet_management.find_pet("P001").get_owner_id(), "O001"
        )

    def test_schedule_appointment(self):
        owner = PetOwner("O001", "Juan Dela Cruz", "09123456789")
        self.owner_management.register_owner(owner)
        pet = PetFactory.create_pet("P001", "Bruno", "Dog", "O001", owner)
        self.pet_management.add_pet(pet)

        appointment = Appointment(
            "A001", "O001", "Bruno", "2026-09-15", "10:00 AM"
        )

        self.assertTrue(
            self.appointment_management.schedule_appointment(appointment)
        )
        self.assertIsNotNone(
            self.appointment_management.find_appointment("A001")
        )
        self.assertEqual(
            self.appointment_management.find_appointment("A001").get_status(),
            "Scheduled"
        )

    def test_cancel_appointment(self):
        appointment = Appointment(
            "A001", "O001", "Bruno", "2026-09-15", "10:00 AM"
        )
        self.appointment_management.schedule_appointment(appointment)

        self.assertTrue(
            self.appointment_management.cancel_appointment("A001")
        )
        self.assertEqual(
            self.appointment_management.find_appointment("A001").get_status(),
            "Cancelled"
        )

    def test_singleton_instance(self):
        db1 = ClinicDatabase.get_instance()
        db2 = ClinicDatabase.get_instance()

        self.assertIs(db1, db2)


if __name__ == "__main__":
    unittest.main()
