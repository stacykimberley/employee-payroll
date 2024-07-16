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

users ={
    'user': 'password'
}

def validate_user():
    while True:
        username = input("Enter your usename: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Login succesful!")
            return True
        else:
            print("Your username or password is incorrect. Please try again.")


def collect_total_hours():
    """
    Ask the user to input total hours data for each employee
    """
    while True:
        print("Please Enter total hours from the previous week.")
        print("Data should be five numbers from emp001 to emp005, separated by commas.")
        print("Like this: 40,40,40,20,20\n")

        data_str = input("Enter total hours here: ")
        
        total_hours_data = data_str.split(",")

        if validate_data(total_hours_data):
            print("Data is valid!")
            break

    return total_hours_data   




def validate_data(values):
    """
    Inside the try converts all string values into floats.
    Raises ValueError if string cannot be converted into float,
    or if there aren't exactly five values.
    """
    try:
        [float(value) for value in values]
        if len(values) != 5:
            raise ValueError(
                f"Five values required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True 


def update_total_hours_worksheet(data):
    """
    Update total hours worksheet, data provided is added to a new row.
    """
    print("Updating total hours worksheet....\n")
    total_hours_worksheet = SHEET.worksheet("total_hours")
    total_hours_worksheet.append_row(data)
    print("Total hours data updates succesfully.\n")


def main():
    """
    Run all program functions
    """
    validate_user()
    data = collect_total_hours()
    total_hours_data = [float(num) for num in data]
    update_total_hours_worksheet(total_hours_data)


main()