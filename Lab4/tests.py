# By: Emmanuel Gabriel M. Visto

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
        owner = PetOwner("20180217", "Mori Calliope", "09012345678")

        self.assertTrue(self.owner_management.register_owner(owner))
        self.assertIsNotNone(self.owner_management.find_owner("20180217"))
        self.assertEqual(
            self.owner_management.find_owner("20180217").get_name(),
            "Mori Calliope"
        )

    def test_add_pet_record(self):
        owner = PetOwner("20210411", "Gawr Gura", "09123456789")
        self.owner_management.register_owner(owner)

        pet = PetFactory.create_pet("20210411", "Ame", "Dog", "20210411", owner)

        self.assertTrue(self.pet_management.add_pet(pet))
        self.assertIsNotNone(self.pet_management.find_pet("20210411"))
        self.assertEqual(
            self.pet_management.find_pet("20210411").get_pet_type(), "Dog"
        )
        self.assertEqual(
            self.pet_management.find_pet("20210411").get_owner_id(), "20210411"
        )

    def test_schedule_appointment(self):
        owner = PetOwner("20210909", "IRyS", "09234567890")
        self.owner_management.register_owner(owner)
        pet = PetFactory.create_pet("20210909", "Hope", "Cat", "20210909", owner)
        self.pet_management.add_pet(pet)

        appointment = Appointment(
            "20210909", "20210909", "Hope", "2026-09-15", "10:00 AM"
        )

        self.assertTrue(
            self.appointment_management.schedule_appointment(appointment)
        )
        self.assertIsNotNone(
            self.appointment_management.find_appointment("20210909")
        )
        self.assertEqual(
            self.appointment_management.find_appointment("20210909").get_status(),
            "Scheduled"
        )

    def test_cancel_appointment(self):
        appointment = Appointment(
            "20201127", "20201127", "Pekora", "2026-09-16", "2:00 PM"
        )
        self.appointment_management.schedule_appointment(appointment)

        self.assertTrue(
            self.appointment_management.cancel_appointment("20201127")
        )
        self.assertEqual(
            self.appointment_management.find_appointment("20201127").get_status(),
            "Cancelled"
        )

    def test_singleton_instance(self):
        db1 = ClinicDatabase.get_instance()
        db2 = ClinicDatabase.get_instance()

        self.assertIs(db1, db2)


if __name__ == "__main__":
    unittest.main()
