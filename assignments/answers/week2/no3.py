number = int(input("Please enter any integer, greater than or equal to 1: "))

while number <= 0:
    number = int(input("Please enter any integer, greater than or equal to 1: "))

for k in range(number, 0, -1):
    if k == number:
       print("*")
    for i in range(1, k-1):
        for j in range(1, i+2):
            print('*',end=" ")
        print("")

    for i in range(k, 0, -1):
        for j in range(1, i+1):
            print("#", end=" ")
        print("")
