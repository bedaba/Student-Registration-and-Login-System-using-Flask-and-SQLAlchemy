# Student-Registration-and-Login-System-using-Flask-and-SQLAlchemy

<h1 align="center">
  <br>
  <a href=""><img src="https://www.iti.gov.eg/assets/images/iti-logo.png" alt="ITI" width="200"></a>
  <br>
  ITI
  <br>
</h1>

<h4 align="center">This is a simple student registration and login system created using Flask and SQLAlchemy. The system includes a registration page where students can create a new account, and a login page where they can log in to their existing account.
.</h4>


![screenshot](https://www.educative.io/v2api/editorpage/6196871006519296/image/6316021754363904)
---------------------------------------------------------------

# Features

    Student registration with validation
    Student login with validation
    SQLite database integration using SQLAlchemy
    Flask flash messaging for success and error messages

# Installation

    Clone the repository: git clone https://github.com/yourusername/student-registration.git
    Install the required packages: pip install -r requirements.txt
    Set up the database: python database.py
    Run the application: python app.py

Usage
# Registration Page

To register a new student, navigate to http://localhost:5000/register. The registration form contains the following fields:

    Username
    Email
    Password
    Confirm Password

Validation is performed on the server-side to ensure that the data is valid. If the validation fails, the user is prompted to provide valid data. If the validation succeeds, the student is added to the database and a success message is flashed. The student is then redirected to the login page.
# Login Page

To log in to an existing student account, navigate to http://localhost:5000/login. The login form contains the following fields:

    Username
    Password

Validation is performed on the server-side to ensure that the data is valid. If the validation fails, the user is prompted to provide valid data. If the validation succeeds and the username and password exist in the database, a success message is flashed and the student is redirected to the home page. If the validation succeeds but the username or password does not exist in the database, an error message is flashed.
---------------------------------------------------------------
## Created BY

[![Bedaba Edward](https://avatars.githubusercontent.com/u/21156712?v=4)](https://github.com/bedaba)

[Bedaba Edward ](https://github.com/bedaba) 
---------------------------------------------------------------
## [License](https://github.com/bedaba/Student-Registration-and-Login-System-using-Flask-and-SQLAlchemy/blob/main/LICENSE)

MIT