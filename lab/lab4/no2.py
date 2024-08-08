number = eval(input("Enter a number: "))

# print(type(number) == int)
# print(isinstance(number, (int)))

if isinstance(number, float):
    choice = eval(input("Which format do u want to display it in \n 1.Floating point \n 2.Scientific \n My choice: "))
    if choice == 1:
        print("Your number", number ,"in flaoting point: ", format(number, ".2f"))
    elif choice == 2:
        print("Your number", number ,"in scientific format: ", format(number, "10.2e"))
    else: 
        print("Please enter a valid choice")
elif isinstance(number, int):
    integer_choice = eval(input("Which format do u want to display this integer in \n 1.Binary \n 2.Octal \n 3.Hexadecimal \n 4.Decimal \n My choice: "))
    if integer_choice == 1:
        print("Binary of", number ,": ",format(number,"5b"))
    elif integer_choice == 2:
        print("Octal of", number ,": ",format(number,"5o"))
    elif integer_choice == 3:
        print("Hexadecimal of", number ,": ",format(number,"5x"))
    elif integer_choice == 4:
        print("Decimal of", number ,": ",format(number, "5d"))
    else: 
        print("Please enter a valid choice")
else:
   print("Please enter a valid number")
