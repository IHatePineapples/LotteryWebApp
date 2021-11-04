# LotteryWebApp

#### Ignore any database/sqlite related crashes.   

    Please make sure of the following:   
        - python is up-to-date   
        - packages are all installed and up-to-date   
        - python from venv/ is up-to-date and so are the apckages   
        - sqlite driver is present   
        - initialise the database through init_db()   
        - should there be errors or crashes related to database, close app, run ini_db() and restart app   


## Summary

The university development team have already implemented a working Python Flask-based lottery web application which they have provided for you for further development. The web application uses the following elements:

    Python Flask Project
    Python Development Server
    SQLite Database 

## Input Validation

#### User Registration form has the following requirements:

    All form fields must be filled.
    Email must be a valid email address.
    Firstname and Lastname must not contain the following characters:  * ? ! ' ^ + % & / ( ) = } ] [ { $ # @ < >
    Phone must be of the form XXXX-XXX-XXXX (including the dashes)
    Password must be between 6 and 12 characters in length.
    Password must contain at least 1 digit, 1 lowercase, 1 uppercase and 1 special character.
    Password and Confirm Password must match.
    PIN Key must be exactly 32 characters in length.
    Relevant validation error messages must be shown.

 
## Error Handling

#### Error handling is required for the following HTTP response status codes:

    400 Bad Request
    403 Forbidden
    404 Not Found
    500 Internal Server Error
    503 Service Unavailable

 
## Cryptography

#### Cryptography is required as follows:

    Hash user passwords on registration before storing in Database.
    Encrypt all lottery draws before storing in Database.
    Decrypt all lottery draws retrieved from Database, for viewing and checking winners.
    Each user must have their own key for encrypting/decrypting draws.
 
## Handling User Logins

### User login must be implemented with the following requirements:

    An application Login Manager
    A login form which takes:
        A valild email address as the username.
        A password.
    All fields must be filled when form is submitted.
    Login menu link must work.
    A fully functioning Login View function.
        If login is successful, users are redirected to the profile page (Note: when implementing role based access control below users with user role should be redirected to profile page; users with admin role should be redirected to admin page).
        If login is unsuccessful, users are invited to try again with an appropriate message.
    Logout menu link must work.
        When logged out, user are redirected to the home page.
 
## Two-Factor Authentication

#### User login has additional requirements to include a time-based PIN into the login process:

    PIN generator setup instructions in Register form. You can use the following:
```html
<div>
    <p><b>Set up One Time Password generator</b></p>
    <ul>
        <li>Download <a href="https://authy.com/download/" target="_blank"><u>Authy</u></a> on your device.</li>
        <li>Select add new account.</li>
        <li>Enter your PIN key.</li>
        <li>Enter name for new account.</li>
        <li>Select token length of 6.</li>
    </ul>
</div>
```
    PIN field in Login form.
    PIN must be 6 digits in length.
    PIN must be verified before user login.

 
## Limiting Invalid Logins

#### User login has the additional requirements:

    Login attempts must be limited to 3.
    Appropriate messages must be displayed for each failed login attempt.
    Login form must be hidden after 3 invalid login attempts have been made.

 
## Access Management

#### Access management has the following requirements for logged-in users.

    User ID must be displayed in place of PLACEHOLDER FOR USER ID on all relevant pages.
    Email must be displayed in place of PLACEHOLDER FOR EMAIL on all relevant pages.
    Firstname must be displayed in place of PLACEHOLDER FOR FIRSTNAME on all relevant pages.
    Lastname must be displayed in place of PLACEHOLDER FOR LASTNAME on all relevant pages.
    Phone must be displayed in place of PLACEHOLDER FOR PHONE on all relevant pages.
    User ID to be updated in place of user_id=1 when adding new draws [TIP: see add_draw() and create_winning_draw() view functions].

 

#### All users, logged in and anonymous (logged out), should have the following:

    Access to home page link.

#### Logged-in users with User role should have the following access:

    View only their own playable draws.
    Check only results of their own played draws.
    Delete only their own played draws when playing again.
    Profile link and page.
    Lottery link, page and all its functions.

#### Logged-in users with Admin role should have the following access:

    Admin link, page and all its functions.

#### All logged-in users should have the following access:

    Account link and page.
    Logout link.

#### Only anonymous users (not logged in) should have the following access:

    Register link.
    Login link.

## Logging

#### Logging has the requirements:

    Appropriate logs to be written to the provided log file lottery.log
    Logging to be filtered to only log:
        User registrations.
        User logins.
        User logouts.
        Invalid login attempts.
        Invalid access attempts.
    Last 10 log entries can be viewed in Administration page starting from most recent.
 
## Role Based Access Control

#### Role Based Access Control must be implemented with the following requirements:

    Only users with User role have access to the following:
        Profile Page.
        Lottery page and all its functions.
    Only users with Admin role have access to the following:
        Admin page and all its functions.

 
## Security Headers

#### HTTP security headers must be implemented with the following requirements:

    A custom Content Security Policy to allow
        The loading of the Bulma CSS framework resourse at https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css (Links to an external site.)
        The loading of the lucky dip JavaScript code defined inside HTML <script> tags [TIP: you will see an example of this when covering randomness].
    The remaining security header configuration can be left as Default.

 
## Secure Randomness

#### All number generation has the following requirements:

    Random number generation must be cryptographically secure.
    Randomly generated numbers and manually inputted numbers must be between 1 and 60.
    Randomly generated draws and manually inputted draws must contain 6 numbers.

 
## Good Coding Practice

#### Entire software application has the following requirements to aid understanding and maintainability:

    All code must be commented sufficiently.
    Code redundancy must be minimised as much as possible.
    Code must be tidy and well formatted.
    Code should be well structured and easy to read with meaningful variable names.
