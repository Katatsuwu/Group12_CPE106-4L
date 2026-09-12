from petOwner import PetOwner

from ownerManagement import OwnerManagement





ownerManagement = OwnerManagement()



print("===== ROXANNE GANDA CLINIC =====")

print("   PET OWNER REGISTRATION")

print()



while True:



  print("\nEnter Pet Owner Information")



  owner_id = input("Owner ID: ")

  name = input("Name: ")

  contact_number = input("Contact Number: ")



  owner = PetOwner(

    owner_id,

    name,

    contact_number

  )



  ownerManagement.register_owner(owner)



  print("\nOwner registered successfully!")



  another = input("\nRegister another owner? (y/n): ")



  if another.lower() != "y":

    break





ownerManagement.display_owners()