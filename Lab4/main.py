from ownerManagement import OwnerManagement


def main():

    ownerManagement = OwnerManagement()

    while True:

        print("\n======================================")
        print("   PAWS AND CARE VETERINARY CLINIC")
        print("        PET OWNER MANAGEMENT")
        print("======================================")

        print("\n[1] Register / Check Pet Owner")
        print("[2] View All Pet Owners")
        print("[3] Search Pet Owner")
        print("[4] Exit")

        choice = input("\nEnter your choice: ")

        # Register or check owner
        if choice == "1":

            ownerManagement.register_new_owner()

        # View all owners
        elif choice == "2":

            ownerManagement.display_owners()

        # Search owner
        elif choice == "3":

            print("\n===== SEARCH PET OWNER =====")

            owner_id = input("Enter Owner ID: ")

            owner = ownerManagement.find_owner(owner_id)

            if owner is not None:
                owner.display_info()
            else:
                print("\nOwner not found.")

        # Exit
        elif choice == "4":

            print("\nThank you for using")
            print("Paws and Care Veterinary Clinic!")
            break

        else:

            print("\nInvalid choice.")
            print("Please enter 1, 2, 3, or 4.")


if _name_ == "_main_":
    main()