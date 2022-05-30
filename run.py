

# Create Contact Info Model
class Person:
    def __init__(self, first, last, email, number, address):
        self.first = first
        self.last = last
        self.email = email
        self.number = number
        self.address = address

    def full_name(self):
        print(f"{self.first} {self.last}")

    # dunder method
    # convert people objects and print them to strings
    # String Magic Method
    def __str__(self):
        return_string = "---------------"
        return_string += f"Name: {self.first} {self.last}"
        return_string += f"Email: {self.email}"
        return_string += f"Contact Number: {self.number}"
        return_string += f"Address: {self.address}"
        return_string += "---------------"
        return return_string


contacts = list()

users_input = ''

# print(contactInfo)
print("Welcome to the address book program")

# While Loop: For Option Selecting
while users_input != "q":
    print("Available Options...")
    print("1) Enter a Contact")
    print("2) Dispay Contact")
    print("q) Quit Program")
    users_input = input("Select Option:")

    if users_input == "1":
        print("Enter your contacts information")

        # Variables
        firstName = input("First name = ")
        lastName = input("last name = ")
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

    elif users_input.lower() == "q":
        break




# Return The Value of the Person
ourContact = Person(firstName, lastName, email, number, address)
print(ourContact)
