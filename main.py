class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name:<15} {self.phone:>10}'

    def update_contact(self, new_name, new_phone):
        self.name = new_name
        self.phone = new_phone


class PhoneBook:
    def __init__(self, filename='phonebook.txt'):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if ',' in line:
                        name, phone = line.split(',', 1)
                        self.contacts.append(Contact(name, phone))
                    else:
                        print(f"Skipping invalid line: {line}")
        except FileNotFoundError:
            print("Phonebook file not found.")

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f'{contact.name},{contact.phone}\n')

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def delete_contact(self, name):
        self.contacts = [
            contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_all(self):
        print(f'{"Name":<15} {"Phone":>10}')
        for contact in self.contacts:
            print(contact)

    def sort_contacts_by_name(self):
        self.contacts.sort(key=lambda contact: contact.name)
        self.save_contacts()


class Application:
    def __init__(self):
        self.phonebook = PhoneBook()

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_choice()
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.find_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.phonebook.display_all()
            elif choice == '5':
                self.phonebook.sort_contacts_by_name()
                print("Contacts sorted by name.")
            elif choice == '6':
                print('Exit')
                break
            else:
                print("Invalid choice.")

    def show_menu(self):
        print("\nPhoneBook Application")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Display All Contacts")
        print("5. Sort Contacts by Name")
        print("6. Exit")

    def get_user_choice(self):
        return input('Enter your choice (only use number): ')

    def add_contact(self):
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        contact = Contact(name, phone)
        self.phonebook.add_contact(contact)
        print("Contact added successfully.")

    def find_contact(self):
        name = input("Enter the name of the contact to search: ")
        contact = self.phonebook.find_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        self.phonebook.delete_contact(name)
        print("Contact deleted ")


if __name__ == "__main__":
    app = Application()
    app.run()
