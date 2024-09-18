def int_to_binary(n):
    if n == 0:
        print("The integer is 0. Conversion is trivial.")
        return '0'
    
    binary_str = ''
    
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str 
        n = n // 2 
    
    return binary_str

def binary_to_int(binary_str):
    integer_value = 0
    
    for i, bit in enumerate(reversed(binary_str)):
        if bit == '1':
            integer_value += 2 ** i 
    
    return integer_value

def main():
    num = int(input("Enter an integer: "))

    if num == 0:
        print("The integer is 0. Nothing to convert.")
        return
    elif num < 0:
        print("Negative numbers are not supported for this conversion.")
        return
    
    binary_str = int_to_binary(num)
    print(f"Binary representation of {num} is: {binary_str}")
    
    converted_back = binary_to_int(binary_str)
    print(f"Converted back to integer: {converted_back}")
    
    if converted_back == num:
        print("Success! The binary to integer conversion matches the original number.")
    else:
        print("Error! Something went wrong with the conversion.")

main()
