contacts = []

def validate_phone(phone):
	if not phone:
		return False

	if phone[0] == "+":
		phone = phone[1:]

	return bool(phone) and all(char.isdigit() or char == "-" for char in phone)


def validate_email(email):
	if email is None or email == "":
		return True
	return "@" in email and "." in email


def find_contact_index(name):
	name = name.strip().lower()
	for index, contact in enumerate(contacts):
		if contact["name"].lower() == name:
			return index
	return None


def format_contact(contact, index=None):
	prefix = f"{index}. " if index is not None else ""
	email = contact.get("email") or "N/A"
	return f"{prefix}Name: {contact['name']} | Phone: {contact['phone']} | Email: {email}"


def print_contacts(contact_list):
	if not contact_list:
		print("No contacts found.")
		return

	print("\n--- Contact Results ---")
	for index, contact in enumerate(contact_list, start=1):
		print(format_contact(contact, index))
	print("-----------------------")


def add_contact(name, phone, email=""):
	if not validate_phone(phone):
		print("Invalid phone number. Use only digits, hyphens, or a leading plus sign.")
		return False

	if not validate_email(email):
		print("Invalid email address. Email must contain '@' and '.'.")
		return False

	if find_contact_index(name) is not None:
		print("A contact with that name already exists.")
		return False

	contacts.append({"name": name.strip(), "phone": phone.strip(), "email": email.strip()})
	print("Contact added successfully.")
	return True


def view_contact(name):
	index = find_contact_index(name)
	if index is None:
		print("Contact not found.")
		return None

	contact = contacts[index]
	print("\n--- Contact Details ---")
	print(format_contact(contact))
	print("-----------------------")
	return contact


def update_contact(name, phone=None, email=None):
	index = find_contact_index(name)
	if index is None:
		print("Contact not found.")
		return False

	if phone is not None and phone != "":
		if not validate_phone(phone):
			print("Invalid phone number. Use only digits, hyphens, or a leading plus sign.")
			return False
		contacts[index]["phone"] = phone.strip()

	if email is not None:
		if not validate_email(email):
			print("Invalid email address. Email must contain '@' and '.'.")
			return False
		contacts[index]["email"] = email.strip()

	print("Contact updated successfully.")
	return True


def delete_contact(name):
	index = find_contact_index(name)
	if index is None:
		print("Contact not found.")
		return False

	removed = contacts.pop(index)
	print(f"Deleted contact: {removed['name']}")
	return True


def Contactss(query):
	query = query.strip().lower()
	matches = [
		contact
		for contact in contacts
		if query in contact["name"].lower()
		or query in contact["phone"].lower()
		or query in contact.get("email", "").lower()
	]
	print_contacts(matches)
	return matches


def list_all_contacts():
	print_contacts(contacts)
	return list(contacts)


def main():
	while True:
		print("\n=== Contact Manager Menu ===")
		print("1. Add Contact")
		print("2. View Contact")
		print("3. Update Contact")
		print("4. Delete Contact")
		print("5. Search Contacts")
		print("6. List All Contacts")
		print("7. Exit")

		choice = input("Choose an option (1-7): ").strip()

		if choice == "1":
			name = input("Enter name: ").strip()
			phone = input("Enter phone number: ").strip()
			email = input("Enter email (optional): ").strip()
			add_contact(name, phone, email)

		elif choice == "2":
			name = input("Enter the contact name to view: ").strip()
			view_contact(name)

		elif choice == "3":
			name = input("Enter the contact name to update: ").strip()
			phone = input("Enter new phone number (press Enter to keep current): ").strip()
			email = input("Enter new email (press Enter to keep current): ").strip()
			update_contact(name, phone if phone else None, email if email else None)

		elif choice == "4":
			name = input("Enter the contact name to delete: ").strip()
			delete_contact(name)

		elif choice == "5":
			query = input("Enter name, phone, or email to search: ").strip()
			Contactss(query)

		elif choice == "6":
			list_all_contacts()

		elif choice == "7":
			print("Exiting Contact Manager.")
			break

		else:
			print("Please enter a number from 1 to 7.")


if __name__ == "__main__":
	main()
