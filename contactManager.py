class ContactManager:
    __contactsList = []

    # Add Contact 
    def addContact(self, name, address, email, phone):
        self.__contactsList.append(Contact(name, address, email, phone))

    # Show All Contacts
    def listContacts(self):
        if not self.__contactsList:
            print('No Contacts Found')
        for contact in self.__contactsList:
            contact.prettyPrint()

    # Delete All Contacts
    def deleteAllContacts(self):
        self.__contactsList = []

    # Delete Contact
    def deleteContact(self):
        for contact in self.__contactsList:
            if contact.name == name and contact.address == address and contact.email == email and contact.phone == phone:
                self.__contactsList.remove(contact)
                return True
        return False

    # Search for contact
    def searchContacts(seld, name, address, email, phone):
        for contact in self.__contactsList:
            if name in contact.name and address in contact.address and email in contact.email and phone in contact.phone:
                contact.prettyPrint()

# Contact Class
class Contact:
    name: None
    Address: None
    Email: None
    Phone: None

    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    def prettyPrint(self):
        print("""Name: %s,
        Address: %s,
        Email: %s,
        Phone: %s""" % (self.name, self.address, self.email, self.phone))
