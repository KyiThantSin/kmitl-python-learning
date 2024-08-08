sum = 0
for _ in range(5):
   value = int(input("Enter an integer: "))
   if value < 0:
       if sum > 0:
           sum = 0
           sum += value
       else:
           sum += value
       print("Current Sum: ", sum)
   else:
       sum += value
       print("Current Sum: ", sum)