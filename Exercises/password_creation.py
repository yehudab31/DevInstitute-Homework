def correct_login(password):

    if password == correct_password:
        return "Welcome!"
    else:
        return "Wrong password."

correct_password = input("Create your password: ")

password_request = input("Enter your password: ")

print(correct_login(password_request))