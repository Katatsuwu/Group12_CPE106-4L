# By: Sean Patrick A. Relucio

from clinicDatabase import ClinicDatabase


class Appointment:
    def __init__(self, appointment_id, owner_id, pet_name, date, time):
        self.__appointment_id = appointment_id
        self.__owner_id = owner_id
        self.__pet_name = pet_name
        self.__date = date
        self.__time = time
        self.__status = "Scheduled"

    def get_appointment_id(self):
        return self.__appointment_id

    def get_owner_id(self):
        return self.__owner_id

    def get_pet_name(self):
        return self.__pet_name

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_status(self):
        return self.__status

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time

    def set_status(self, status):
        self.__status = status

    def display_info(self):
        return (
            f"Appointment ID: {self.__appointment_id}\n"
            f"Owner ID: {self.__owner_id}\n"
            f"Pet Name: {self.__pet_name}\n"
            f"Date: {self.__date}\n"
            f"Time: {self.__time}\n"
            f"Status: {self.__status}"
        )


class AppointmentManagement:

    def __init__(self, database=None):
        self.database = database or ClinicDatabase.get_instance()

    @property
    def appointments(self):
        return self.database.appointments

    def schedule_appointment(self, appointment):
        if self.find_appointment(appointment.get_appointment_id()) is not None:
            return False
        self.database.add_appointment(appointment)
        return True

    def get_appointments(self):
        return self.database.appointments

    def find_appointment(self, appointment_id):
        return self.database.find_appointment(appointment_id)

    def cancel_appointment(self, appointment_id):
        appointment = self.find_appointment(appointment_id)

        if appointment is None:
            return False

        appointment.set_status("Cancelled")
        self.database.save_data()
        return True

    def update_status(self, appointment_id, status):
        valid_statuses = ["Scheduled", "Completed", "Cancelled"]

        if status not in valid_statuses:
            return False

        appointment = self.find_appointment(appointment_id)

        if appointment is None:
            return False

        appointment.set_status(status)
        self.database.save_data()
        return True

    def display_appointments(self):
        if not self.appointments:
            print("No scheduled appointments.")
            return

        print("\n===== APPOINTMENT SCHEDULES =====")

        for appointment in self.appointments:
            print(appointment.display_info())
            print("------------------------------")
