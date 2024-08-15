import math
number = int(input("Enter the number of lines: "))

for i in range(1, math.ceil(number/2) +1 ):
    for j in range(i, 0 , -1):
        print(2 ** (j - 1), end=" ")
    print()

for i in range(math.floor(number/2), 0, -1):
    for j in range(i, 0 , -1):
        print(2 ** (j - 1), end=" ")
    print()