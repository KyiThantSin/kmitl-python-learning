# rock paper scissor
import random

print("Please enter a number")
user = int(input("scissor (0), rock(1), paper(2): "))
computer = random.randint(0,3)

while user < 0 or user > 2:
      print("Please enter a valid number")
      user = int(input("scissor (0), rock(1), paper(2): "))              


if computer == 0 and user == 2:
    print("The computer is scissor. You are a paper. Computer Win :< ") 
elif computer == 1 and user == 0:
    print("The computer is rock. You are a scissor. Computer Win :< ")
elif computer == 2 and user == 1:
    print("The computer is paper. You are a rock. Computer Win :< ")
elif user == 0 and computer == 2:
    print("You are scissor. Computer is a paper. You Win!! ") 
elif user == 1 and computer == 0:
    print("You are rock. Computer is a scissor. You Win!! ") 
elif user == 2 and computer == 1:
    print("You are paper. Computer is a rock. You Win!! ") 
elif user == 0 and computer == 0:
    print("The computer is scissor. You are scissor too. It is a draw")
elif user == 1 and computer == 1:
    print("The computer is rock. You are rock too. It is a draw")
elif user == 2 and computer == 2:
    print("The computer is paper. You are paper too. It is a draw")


