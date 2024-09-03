number = int(input("Enter a number: "))

while number < 0:
    number = int(input("Enter a number: "))

def reversed_order(number):
    number_string = str(number)
    reversed_number = ""
    for i in range(len(number_string)-1, -1, -1):
        reversed_number += str(number_string[i])
    return int(reversed_number)
        
print(reversed_order(number))
