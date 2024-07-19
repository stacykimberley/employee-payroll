# Automated Employee Payroll

![Website Mockup](assets/images/readme/mockup.png)

[Here is the live website link!](https://employee-payroll-e73ff1f1c097.herokuapp.com/)

[Here is the link to the live GoogleSheet](https://docs.google.com/spreadsheets/d/1YnG2qfR0p6KZsm26ygfB5IRJA8U38uFi2xsBnKnsvrE/edit?usp=sharing)

# Login details

Username : user

Password : password

# Table of Contents

- [Purpose](#Purpose)
- [Goal](#Goal)
- [UX Design](#UX-Design)
- [FlowChart](#FlowChart)
- [Colorama](#Colorama)
- [Python Logic](#Python-logic)
- [APIs used](#APIs-used)
- [Testing](#Testing)
- [Technologies used](#Technologies-used)




# Purpose

The Employee Payroll App is a comprehensive solution designed to streamline and simplify the payroll process for a small business owner with 5 employees currently.The owner does payroll themself, by entering entering total and overtime hours weekly to create pay stubs for al employees. At the moment since all employees are earning close to minimum wage, there's only 1 deduction; a 20% tax rate. The app ensures accurate and timely payroll processing, reduces administrative workload, and enhances compliance with labor laws and regulations. With user-friendly interfaces and robust functionality, the Employee Payroll App is an essential tool for modern workforce management.

# Goal

The goal of the app is to allow the business owner to create weekly pay stubs for their 5 employees.

# UX Design

## Target audience

Small business owner with only employees earning close to minimum wage at a tax rate of 20%

## User stories

### As a first time user

- I want to enter my username and password for authentication so that a user without the login details cannot access payroll information.
- I want to enter total hours for my employees.
- I want to enter overtime hours for my employees.
- I want instructions for entering data to be easy to understand.
- I want total hours and overtime hours to be updated to a spreadsheet.
I want gross pay to be calculated.
- I want net pay to be calculated by deducting the 20% tax rate.
- I want to create pay stubs for all my employees.

### As a returning user

- I want to be able to add more employees if I hire additional ones.
- I want to be able to calculate net pay for employees in a different tax bracket.
- I want to create pay stubs for all my employees

# Design

## FlowChart

![FlowChart](assets/images/readme/employee_payroll_chart.png)

1. **Validate user:**
- Input username and password.
- Validate against stored credentials.
2. **Input total hours:**
- Input total hours for all employees.
3. **Update total hours worksheet:**
- Insert total hours into GoogleSheet.
4. **Input overtime hours:**
- Input overtime hours for all employees.
5. **Update overtime hours worksheet:**
- Insert overtime hours into GoogleSheet.
6. **Calculate gross pay:**
- Calculate each employee's gross pay.
7. **Update gross pay worksheet**
- Update GoogleSheet with calculated gross pay far all employees.
8. **Calculate net pay:**
- Calculate each employee's net pay.
9. **Update net pay worksheet:**
- Update GoogleSheet with calculated net pay far all employees.
10. **Create pay stubs:**
- Generate and display pay stubs for all employees

## Colorama

The application uses the colorama library for changing the color of terminal text to enhance user experience with clear visual feedback:

1. Green for valid data messages.

![Green](assets/images/readme/colorama_green.png)

2. Red for invalid data messages.

![Red](assets/images/readme/colorama_red.png)

# Application Features

## Python logic
- User Validation: Ensures secure login for administrators.
- total hours Input: Collects total hours for all employees.
- overtime hours Input: Collects overtime hours for all employees.
- Data Insertion: Adds total and overtime to Google Sheets.
- Gross and net pay calculation: Calculates gross and net pay for all employees.
- Gross and net pay update: Updates Google Sheets with gross and net pay.
- Pay stubs generation: Produces pay stubs for all employees.

## APIs used
- Google Sheets API: For storing, retrieving, and updating employee data.

## Technologies:

The app is developed using Python.

## Future Features

- Give the admin an option to add/ remove an employee
- Calculate a tax deduction of 40% for employees earning over $40, 000 a year.
- Have a separate input for holiday hours.

# Testing

**No Errors Where Found**

![python validation](assets/images/readme/testing.png)

[CI Python Linter](https://pep8ci.herokuapp.com/#)

## User story testing

![User story testing](assets/images/readme/first_time_user_testing.png)

# Feature testing 

![Website Mockup](assets/images/readme/feature_testing.png

## API Setup

1. Google Cloud Project:

  - Go to the Google Cloud Console.
  - Create a new project or select an existing one.
2.  Enable APIs:

  - Enable the Google Sheets API and Google Drive API for your project:
  - Navigate to the API Library.
  - Search for "Google Sheets API" and "Google Drive API".
  - Click on each and enable them.

3. Create a Service Account:

  - Go to the Service Accounts page.
  - Click "Create Service Account".
  - Provide a name and description for the service account.
  - Click "Create and Continue".
  - Grant Roles to the Service Account:

4. Assign the role of "Editor" to the service account.
  - Click "Continue" and then "Done".

5. Create and Download a Service Account Key:

  - Click on the service account you just created.
  - Go to the "Keys" tab.
  - Click "Add Key" and select "Create new key".
  - Choose JSON and download the key file. Save it as creds.json in your project directory.

6. Share Google Sheets with Service Account:

  - Open your Google Sheet.
  - Click "Share".
  - Enter the service account email (found in the creds.json file) and give it "Editor" access.

## Deployment

### Heroku

1. Sign into [Heroku](https://dashboard.heroku.com/apps)
2. On the right side click **New** and select **Create new app**
3. Create a new Heroku app with a unique name. Heroku will generate a random name if you don't specify one and select your region.
4. Click **Create app**
5. Close to the top select **Settings**, click on *Reveal Config Vars**
  - On **Key** and **Value** input fields enter PORT and Paste everything copied from the **creds.json** folder in your gitpod workspace(respectively).
6. Click **add** to create another set of KEY and VALUE.
  - In the input fields add KEY: PORT, VALUE: 8000
7. At the bottom, click **Add buildpack**, from the options select **python** and **nodejs** + **add buildpack** after selecting each.
8. Close to the top where you clicked **Settings** this time click **Deploy**, click **connect to github**.
  - search for the name of the repository you want to deploy and click **connect**
9. Click **deploy branch**

## Technologies used

- GitHub to store the source code.
- Gitpod chosen IDE to develop the website.
- Microsoft Word to create testing tables.
- Code Institute's Gitpod Template to generate the workspace for the project.
- Code institute learnings for general guidance.
- Techsini to create mockup of website on different iOS devices.
- Lucidchart to create the flowchart
- CI python linter to test |Python code

## Credits

### Code

- Code to add username and password from Hazel Hawadi
- Python learnings from Code institute lessons and modified.
- Code Institute Love Sandwiches run through lessons and modified.

## Acknowledgements

I would like to express my gratitude to the following individuals for their contributions and support:

My mentor, Ronan McClelland for great support, advice, learning reasources and guidance throughout this project.

My sister Hazel Hawadi for moral support and help with coding.

Amy Richardson(Cohort Facilitator) for her regular check-ins and support.




