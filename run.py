import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contactBook')

# Access the contact information
directory = SHEET.worksheet('Directory')
contactInfo = directory.get_all_values()

# print(contactInfo)

print("Welcome to the address book program")
print("Please enter your contact's information")

# Variables
firstName = input("First name = ")
lastName = input("last name = ")
email = input("Email Address = ")
number = int(input("Number = "))
address = input("Enter Address = ")

print('Thank you, Information received')