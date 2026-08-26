def approved_access(correct):

    if user_name in approved_names and age >=18 and password == correct_password:
        print(f"Welcome, {user_name}! You are {age} years old.")
    else: 
        print("Access denied.")

approved_names = ['Yehuda', 'Sarah', 'David',]

user_info = {

user_name = input("Enter your name: " )

age = int(input("How old are you? "))


}

correct_password = "python123"

password_attempt = input("Enter your password: ")

approved_access(user_name, age, password_attempt)