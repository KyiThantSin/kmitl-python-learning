character = input("Please enter a character: ")

if 0x30 <= ord(character) <= 0x39:
    print(character, "is a Numeric Number.")
elif 0x41 <= ord(character) <= 0x54:
    print(character, "is a Capital Letter and its small-case lettter is ", character.lower())
elif 0x61 <= ord(character) <= 0x7A:
    print(character, "is a Small-case Letter and its capital lettter is ", character.upper())
else:
    print(character, "s a Special Character.")


