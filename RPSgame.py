import random
import os
rock =  """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Greetings
print("Welcome to the Rock, Paper, Scissors game!!!")

#User Choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("Ops! You must type a number between 0 and 2!")
    os.system("pause")


#Computer Random Choice
computers_choice = random.randint(0 , 2)
if computers_choice == 0:
    print("Computer chose: ",rock)
if computers_choice == 1:
    print("Computer chose: ",paper)
if computers_choice == 2:
    print("Computer chose: ",scissors)

#Win/Lose/Tie Conditional
if user_choice == 0 and computers_choice == 2:
    print("You Win!")
elif user_choice == 1 and computers_choice == 0:
    print("You Win!")
elif user_choice == 2 and computers_choice == 1:
    print("You Win!")
elif user_choice == computers_choice:
    print("Tie!")
else: 
    print("Computer Wins!")

'''
Notes:
paper wins rock
rock wins scissors
scissors wins paper

made by Gabriel Santos ☕
GitHub: santosgabrieldev (https://github.com/santosgabrieldev)
'''
