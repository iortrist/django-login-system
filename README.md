# Django Login System
Basic login system

## Functionality
- User registration
    - Checks if username already exists
    - Checks if username is less than 4 characters
    - Checks if username is alpha-numeric
    - Checks if password and password confirmatation matches
    - Checks if password is less than 8 characters
    - Checks if email already exists
    - Welcome message is sent via email for every succcessful registration
- User login
    - Checks if credential entered is valid
- Restrict authenticated user to access login and registration pages