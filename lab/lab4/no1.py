score = int(input("Enter a score in the range from 0 to 100: "))

while score < 0 or score > 100:
   print("Invalid Input")
   score = int(input("Enter a score in the range from 0 to 100: "))


if 80 <= score <= 100:
    print("Your grade: A")
elif 70 <= score < 80:
    print("Your grade: B")
elif 60 <= score < 70:
    print("Your grade: C")
elif 50 <= score < 60:
    print("Your grade: D")
elif score < 50:
    print("Your grade: F")
else: 
    print("Invalid Input")