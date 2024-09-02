number = int(input("Enter number between 0-999: "))

def display_pronunciation(number):
    one_to_ten = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    ten_to_nineteen = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenty_to_ninety = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number == 0:
        return "zero"
    elif 1 <= number <= 10:
        return one_to_ten[number]
    elif 11 <= number <= 19:
        return ten_to_nineteen[number % 10]
    elif 20 <= number <= 99:
        tens = number // 10
        ones = number % 10
        if ones == 0:
            return twenty_to_ninety[tens]
        else:
            return twenty_to_ninety[tens] + "-" + one_to_ten[ones]
    elif 100 <= number <= 999:
        hundreds = number // 100
        remainder = number % 100
        if remainder == 0:
            return one_to_ten[hundreds] + " hundred"
        elif 1 <= remainder <= 10:
            return one_to_ten[hundreds] + " hundred and " + one_to_ten[remainder]
        elif 11 <= remainder <= 19:
            return one_to_ten[hundreds] + " hundred and " + ten_to_nineteen[remainder % 10]
        else:
            tens = remainder // 10
            ones = remainder % 10
            if ones == 0:
                return one_to_ten[hundreds] + " hundred and " + twenty_to_ninety[tens]
            else:
                return one_to_ten[hundreds] + " hundred and " + twenty_to_ninety[tens] + "-" + one_to_ten[ones]
    else:
        return "I don't know."

print(display_pronunciation(number))

