n = eval(input("Enter a number n: "))
guess = n / 2

for i in range (0,5):
    temp = n / guess
    guess = ( guess + temp ) / 2
print("Approximate square root of",n,"after 5 iterations: ", format(guess,".3f"))

for i in range (0,6):
    temp = n / guess
    guess = ( guess + temp ) / 2
print("Approximate square root of",n,"after 6 iterations: ", format(guess,".3f"))

for i in range (0,7):
    temp = n / guess
    guess = ( guess + temp ) / 2
print("Approximate square root of",n,"after 7 iterations: ", format(guess,".3f"))



