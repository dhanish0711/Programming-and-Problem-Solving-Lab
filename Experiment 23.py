"""
Write a Python program that functions as a simple phone book manager with a menu-driven interface. The program prompts the user to choose from the following options:
Add Contact
Remove Contact
Display
Quit

The program uses a dictionary to store contact information, where the contact name serves as the key and the associated phone number as the value. The user can add a contact, remove a contact, display the current contacts, or exit the program.
"""

phonebook = {}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice (1-4): ").strip()
	if choice == "1":
		name = input("Name: ").strip()
		phone = input("Phone number: ").strip()
		phonebook[name] = phone
	elif choice == "2":
		name = input("Name: ").strip()
		if name in phonebook:
			del phonebook[name]
		else:
			print("Not found")
	elif choice == "3":
		print(phonebook)
	elif choice == "4":
		break
	else:
		print("Invalid")
