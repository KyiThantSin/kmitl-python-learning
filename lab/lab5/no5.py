character = input("Please enter a character: ")

def check_character(value):
    if 0x30 <= ord(value) <= 0x39:
        print(value, "is a Numeric Number.")
    elif 0x41 <= ord(value) <= 0x54:
        print(value, "is a Capital Letter and its small-case lettter is ", value.lower())
    elif 0x61 <= ord(value) <= 0x7A:
        print(value, "is a Small-case Letter and its capital lettter is ", value.upper())
    elif ord(value) == 9:
        print("Good Bye, See you Tomorrow")
    else:
        print(value, "s a Special Character.")
    
check_character(character)

while ord(character) != 9:
    character = input("Please enter a character: ")
    if ord(character) == 9:
        print("Good Bye, See you Tomorrow")
        break
    else:
        check_character(character)


