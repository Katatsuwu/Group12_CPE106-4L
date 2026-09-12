from ownerManagement import OwnerManagement
from petManagement import PetManagement
from petFactory import PetFactory
from appointmentManagement import Appointment, AppointmentManagement
from clinicDatabase import ClinicDatabase


def main():
    database = ClinicDatabase.get_instance()
    ownerManagement = OwnerManagement(database)
    petManagement = PetManagement(database)
    appointmentManagement = AppointmentManagement(database)

    while True:        print("\n===========================================")
        print(" 🐾🏥 PAWS AND CARE VETERINARY CLINIC 🏥🐾")
        print("===========================================")
        print("[1] Register Pet Owner")
        print("[2] View All Pet Owners")
        print("[3] Add Pet Record")
        print("[4] View Pet Records")
        print("[5] Schedule Appointment")
        print("[6] View Appointments")
        print("[7] Cancel Appointment")
        print("[8] Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            ownerManagement.register_new_owner()

        elif choice == "2":
            ownerManagement.display_owners()

        elif choice == "3":
            print("\n===== ADD PET RECORD =====")
            pet_id = input("Enter Pet ID: ")
            name = input("Enter Pet Name: ")
            pet_type = input("Enter Pet Type (Dog/Cat/Bird/Rabbit): ")
            owner_id = input("Enter Owner ID: ")

            owner = ownerManagement.find_owner(owner_id)
            if owner is None:
                print("\nOwner not found.")
                continue

            try:
                pet = PetFactory.create_pet(
                    pet_id, name, pet_type, owner_id, owner
                )
            except ValueError as error:
                print(f"\n{error}")
                continue

            if petManagement.add_pet(pet):
                print("\nPet added successfully!")
                pet.display_info()
            else:
                print("\nPet ID already exists.")

        elif choice == "4":
            petManagement.display_pets()

        elif choice == "5":
            print("\n===== SCHEDULE APPOINTMENT =====")
            appointment_id = input("Enter Appointment ID: ")
            owner_id = input("Enter Owner ID: ")
            pet_name = input("Enter Pet Name: ")
            date = input("Enter Date: ")
            time = input("Enter Time: ")

            appointment = Appointment(
                appointment_id, owner_id, pet_name, date, time
            )

            if appointmentManagement.schedule_appointment(appointment):
                print("\nAppointment scheduled successfully!")
            else:
                print("\nAppointment ID already exists.")

        elif choice == "6":
            appointmentManagement.display_appointments()

        elif choice == "7":
            appointment_id = input("\nEnter Appointment ID: ")

            if appointmentManagement.cancel_appointment(appointment_id):
                print("\nAppointment cancelled successfully!")
            else:
                print("\nAppointment not found.")

        elif choice == "8":
            print("\nThank you for using")
            print("Paws and Care Veterinary Clinic!")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
