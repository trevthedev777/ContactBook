import contactManager


class ConsoleInputManager:
    "This static classs manages the input"
    contactManager = None

    def __init__(self):
        self.contactManager = contactManager.ContactManager()

    # Add Contact Details
    def __getContactInformationFromUser(self):
        # Ask for name
        print("Please give the Name of the contact")
        name = input()
        # Ask for address
        print("Please enter the address of this person")
        address = input()
        # Ask for email address
        print("What is their email address?")
        email = input()
        # Ask for phone number
        print("What is their contact number?")
        phone = input()

    def __addContactToContacts(self):
        name, address, email, phone = self.__getContactInformationFromUser()
        contact =  self.contactManager.addContact(name, address, email, phone)

