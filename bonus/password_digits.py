"""
Create a script that asks the user to enter a password.
Then create a function that checks the strength of the user password.
The function should return Strong Password if all of the following conditions are true:

Eight or more characters

At least one uppercase letter.

At least one digit.
"""


user_password = input("Enter new password: ")


def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength(user_password))