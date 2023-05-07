""" 
Python console application that uses the Repository Design Pattern to 
manage a list of contacts. The application will allow the user to 
add, update, and delete contacts, and display a list of all contacts.
"""

class Contact:
    """
    Class that represents a contact with 
    a name, phone number, and email address.
    """
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} ({self.phone}, {self.email})'
    
class ContactRepository:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def update_contact(self, name, phone, email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                break
            
    def upsert_contact(self, name, phone, email):
        for contact in self.contacts:
            if contact.name == name:
                self.update_contact(name, phone, email)
                return
        contact = Contact(name, phone, email)
        self.add_contact(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def get_all_contacts(self):
        return self.contacts

def main():
    repo = ContactRepository()

    while True:
        print('\nWelcome to the Contact Manager!\n')
        print('1. Add a contact')
        print('2. Update a contact')
        print('3. Delete a contact')
        print('4. List all contacts')
        print('5. Exit\n')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            contact = Contact(name, phone, email)
            repo.add_contact(contact)
            print('Contact added successfully!')

        elif choice == '2':
            name = input('Enter name of contact to update: ')
            phone = input('Enter new phone: ')
            email = input('Enter new email: ')
            repo.update_contact(name, phone, email)
            print('Contact updated successfully!')

        elif choice == '3':
            name = input('Enter name of contact to delete: ')
            repo.delete_contact(name)
            print('Contact deleted successfully!')

        elif choice == '4':
            contacts = repo.get_all_contacts()
            if len(contacts) == 0:
                print('No contacts found.')
            else:
                print('Contacts:')
                for contact in contacts:
                    print(contact)

        elif choice == '5':
            break

        else:
            print('Invalid choice. Please try again.')

    print('\nGoodbye!')


if __name__ == '__main__':
    main()
