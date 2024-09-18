def calculate_char_frequency(text):
    text = text.replace(" ", "")
    
    total_length = len(text)
    
    unique_chars = []
    
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
            
    print("\nCharacter Frequency Table")
    print("char\tpercentage")
    
    for char in unique_chars:
        count = 0
        for c in text:
            if c == char:
                count += 1
        percentage = (count / total_length) * 100
        print(f"{char}\t{percentage:.2f}%")
    
user_input = input("Enter some text: ")
calculate_char_frequency(user_input)
