def isAnagram(String1, String2):
    if len(String1) != len(String2):
        return False

    char_count1 = {}
    char_count2 = {}

    for char in String1:
        char_count1[char] = char_count1.get(char, 0) + 1

    for char in String2:
        char_count2[char] = char_count2.get(char, 0) + 1

    return char_count1 == char_count2

print(isAnagram("silent", "listen")) 
print(isAnagram("joy", "joke"))     