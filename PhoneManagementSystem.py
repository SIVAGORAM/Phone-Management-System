import os

# Define a class for contacts
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"

# Define a class for the contact manager
class ContactManager:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone = line.strip().split(',')
                    contact = Contact(name, phone)
                    self.contacts.append(contact)

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone}\n")

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.save_contacts()

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        return found_contacts

    def list_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")

# Function to display menu and handle user input
def main_menu(contact_manager):
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_manager.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            found_contacts = contact_manager.search_contact(name)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(contact)
            else:
                print(f"No contacts found with name '{name}'.")
        elif choice == '3':
            contact_manager.list_contacts()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
1
if __name__ == "__main__":
    contact_manager = ContactManager("contacts.txt")
    main_menu(contact_manager)
