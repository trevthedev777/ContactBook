# Create Contact Info Model
class Person:
    def __init__(self, first, last, email, number, address):
        self.first = first
        self.last = last
        self.email = email
        self.number = number
        self.address = address

    def full_name(self):
        return f"{self.first} {self.last}"

    # dunder method
    # convert people objects and print them to strings
    # String Magic Method
    def __str__(self):
        return_string = "---------------"
        return_string += f" Name: {self.first} {self.last} |"
        return_string += f" Email: {self.email} |"
        return_string += f" Contact Number: {self.number} |"
        return_string += f" Address: {self.address} "
        return_string += "---------------"
        return return_string


contacts = list()

users_input = ''

# print(contactInfo)
print("Welcome to the address book program")
print("===================================")
print("")

# While Loop: For Option Selecting
while users_input != "q":
    print("Available Options...")
    print("==================")
    print("")
    print("|1| Enter a Contact")
    print("")
    print("|2| Display Contact")
    print("")
    print("|3| Find Contact")
    print("")
    print("|q| Quit Program")
    print("")
    print("==================")
    users_input = input("Select Option:")

    if users_input == "1":
        print("Enter your contacts information")

        # Variables
        firstName = input("First name = ")
        lastName = input("Last name = ")
        email = input("Email Address = ")
        number = int(input("Number = "))
        address = input("Enter Address = ")

        ourContact = Person(firstName, lastName, email, number, address)
        contacts.append(ourContact)
             
        print('Thank you, Information received')

    elif users_input == "2":
        for contact in contacts:
            print(contact)
        print("All contacts displaying, hit enter to continue")

    elif users_input == "3":
        search = input("Search for a contact....\n")
        for contact in contacts:
            # .full_name() allows us to search for the 
            # name in first or last name
            if search in contact.full_name():
                print(contact)
    
    elif users_input.lower() == "q":
        break

# Return The Value of the Person
ourContact = Person(firstName, lastName, email, number, address)

