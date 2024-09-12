s1 = input("Enter a first string: ")
s2 = input("Enter a second string: ")

def LCS(s1, s2): 
    longer = ""
    word = ""
    for x in range(len(s1)):
        for y in range(len(s2)):
            if s2[y] == s1[x]:
                y1 = y
                x1 = x
                while y1 < len(s2) and x1 < len(s1) and s2[y1] == s1[x1]:
                    word += s2[y1]
                    y1 += 1
                    x1 += 1
            if len(word) > len(longer):
                longer = word
            word = ""
    return longer

print(LCS(s1,s2))