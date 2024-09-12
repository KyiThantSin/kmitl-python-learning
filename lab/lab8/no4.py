user_first_name = input("Enter the user first name: ")
user_last_name = input("Enter the user last name: ")
user_gender = input("Enter the gender(m/f): ").lower()

while user_gender != "m" and user_gender != "f":
    print("please enter a valid gender")
    user_gender = input("Enter the gender: ") 

result = ("F" if user_gender.lower() == "f" else "M") + user_last_name[0] + user_first_name[0:7]
print("Your user name", result.upper())