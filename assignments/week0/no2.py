number = int(input("Enter a fout-digit integer: "))

if 0000 <= number <= 9999:
    number_str = str(number)
    reversed_number = ""
    for digit in number_str:
                    reversed_number = digit + reversed_number
    print("The number in reverse order:", reversed_number)
else:
    print("Invalid input. Please enter a four-digit integer.")