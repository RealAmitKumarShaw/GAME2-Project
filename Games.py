import random

'''
1 for stone
-1 for paper
0 for scissor
'''
computer = random.choice([-1, 0, 1])
youDict = {"st": 1, "p": -1, "sc": 0}
reversedDict = {1: "Stone", -1: "Paper", 0: "Scissor"}

youstr = input("Enter your choice: ")
you = youDict[youstr]

print(f"You chose {reversedDict[you]} ")
print(f"Computer chose {reversedDict[computer]}")

if(computer == -1 and you == 1):
  print("You lose!")
elif(computer == -1 and you == 0):
  print("You Win!")
elif(computer == 0 and you == 1):
  print("You win!")
elif(computer == 0 and you == -1):  
  print("You lose!")
elif(computer == 1 and you == -1):
  print("You win!")
elif(computer == 1 and you == 0):
  print("You lose!")
else:
  print("Its a tie!")

