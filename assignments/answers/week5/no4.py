def calculate_isbn_10_checksum(isbn_9_digits):
    checksum = 0
    
    for i in range(9):
        checksum += int(isbn_9_digits[i]) * (i + 1)
    
    checksum = checksum % 11
    
    return 'X' if checksum == 10 else str(checksum)

isbn_input = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if len(isbn_input) == 9 and isbn_input.isdigit():
    checksum = calculate_isbn_10_checksum(isbn_input)
    isbn_10 = isbn_input + checksum
    print("Your ISBN-10 number is:", isbn_10)
else:
    print("Invalid input! Please enter exactly 9 digits.")
