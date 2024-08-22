number = int(input("Enter number: "))

def sum_of_digit(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print("sum = ",sum_of_digit(number))