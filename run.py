# import gspread
# from google.oauth2.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('contactBook')

# # Access the contact information
# directory = SHEET.worksheet('Directory')
# contactInfo = directory.get_all_values()

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
        return_string = "---------------\n"
        return_string += f"Name: {self.first} {self.last}\n"
        return_string += f"Email: {self.email}\n"
        return_string += f"Contact Number: {self.number}\n"
        return_string += f"Address: {self.address}\n"
        return_string += "---------------\n"
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

    if users_input == 1:
        print("Enter your contacts information")

        # Variables
        firstName = input("First name = ")
        lastName = input("last name = ")
        email = input("Email Address = ")
        number = int(input("Number = "))
        address = input("Enter Address = ")

        ourContact = Person(firstName, lastName, email, number, address)

        print('Thank you, Information received')


print("Please enter your contact's information")



# Return The Value of the Person
ourContact = Person(firstName, lastName, email, number, address)
print(ourContact)
