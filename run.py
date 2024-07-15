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
SHEET = GSPREAD_CLIENT.open('employee_payroll')

def collect_total_hours():
    """
    Ask the user to input total hours data for each employee
    """
    print("Please Enter total hours from the previous week.")
    print("Data should be five numbers from emp001 to emp005, separated by commas.")
    print("Like this: 40,40,40,20,20\n")

    data_str = input("Enter total hours here: ")
    print(f"The hours provided are {data_str}")

collect_total_hours()    
