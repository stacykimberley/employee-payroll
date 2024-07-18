import gspread
from google.oauth2.service_account import Credentials 
from colorama import init, Fore

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
            print(Fore.GREEN + "Login succesful!" + Fore.RESET)
            return True
        else:
            print(Fore.RED + "Your username or password is incorrect. Please try again." + Fore.RESET)


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
            print(Fore.GREEN + "Data is valid!" + Fore.RESET)
            break

    return total_hours_data   


def collect_overtime_hours():
    """
    Ask the user to input overtime hours data for each employee
    """
    while True:
        print("Please Enter overtime hours from the previous week.")
        print("Data should be five numbers from emp001 to emp005, separated by commas.")
        print("Like this: 1,2,3,4,4.5\n")

        data_str = input("Enter overtime hours here: ")
        
        overtime_hours_data = data_str.split(",")

        if validate_data(overtime_hours_data):
            print(Fore.GREEN + "Data is valid!" + Fore.RESET)
            break

    return overtime_hours_data

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


def update_worksheet(data, worksheet):    
    """
    Receives a list of data to be inserted into a worksheet
    Relevant worksheet is updated with provided data
    """
    print(f"Updating {worksheet} worksheet....\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated succesfully.\n")


def calculate_gross_pay_data(total_hours_row, overtime_hours_row):
    """
    Multiply total hours by hourly rate
    Multiply overtime hours by hourly rate by 1.5
    Gross pay is the total of total hours and overtime hours pay
    """
    print("Calculating gross pay...\n")
    hourly_rate = SHEET.worksheet("hourly_rate").get_all_values()
    hourly_rate_row = [float(rate) for rate in hourly_rate[-1]]
    
    gross_pay_data = []
    for hourly_rate, total_hours, overtime_hours in zip(hourly_rate_row, total_hours_row, overtime_hours_row):
        gross_pay = (hourly_rate * total_hours) + (hourly_rate * overtime_hours * 1.5)
        gross_pay_data.append(gross_pay)
    
    return gross_pay_data   


def calculate_net_pay_data(gross_pay_row):
    """
    Multiply gross pay by 0.8 to subtract tax
    All employees pay a tax rate of 20%
    """
    print("Calculating net pay...\n")
    net_pay_data = [gross_pay * 0.8 for gross_pay in gross_pay_row]
    return net_pay_data


def create_pay_stub(total_hours_row, overtime_hours_row, gross_pay_row, net_pay_row):
    """
    Display pay stub with details including ID, total hours worked,
    overtime hours worked, gross pay, and net pay.
    """
    print("Employee Details:\n")
    employee_ids = ['emp001', 'emp002', 'emp003', 'emp004', 'emp005']
    for emp_id, total_hours, overtime_hours, gross_pay, net_pay in zip(employee_ids, total_hours_row, overtime_hours_row, gross_pay_row, net_pay_row):
        print(f"Employee ID: {emp_id}")
        print(f"Total Hours Worked: {total_hours}")
        print(f"Overtime Hours Worked: {overtime_hours}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")
        print("-" * 20)    
     

def main():
    """
    Run all program functions
    """
    validate_user()
    data = collect_total_hours()
    total_hours_data = [float(num) for num in data]
    update_worksheet(total_hours_data, "total_hours")
    data = collect_overtime_hours()
    overtime_hours_data = [float(num) for num in data]
    update_worksheet(overtime_hours_data, "overtime_hours")
    new_gross_pay_data = calculate_gross_pay_data(total_hours_data, overtime_hours_data)
    update_worksheet(new_gross_pay_data, "gross_pay")
    new_net_pay_data = calculate_net_pay_data(new_gross_pay_data)
    update_worksheet(new_net_pay_data, "net_pay")
    create_pay_stub(total_hours_data, overtime_hours_data, new_gross_pay_data, new_net_pay_data)


print("Hello! Welcome to Employee Payroll Data Automation.")
main()