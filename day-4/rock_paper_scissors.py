
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
user= input("rock, paper, or scissors?: \n").lower()

opcoes=["rock","paper","scissors"]
computerchoice=random.choice(opcoes)
print(computerchoice)

if computerchoice=="rock":
    print(rock)
elif computerchoice=="paper":
    print(paper)
else:
    print(scissors)

if user =="rock" and computerchoice == "paper":
    print("You lose!")
elif user =="rock" and computerchoice == "scissors":
    print("You win!")
elif user =="rock" and computerchoice == "rock":
    print("its a tie!")
elif user =="paper" and computerchoice == "rock":
    print("You win!")
elif user =="paper" and computerchoice == "scissors":
    print("You lose!")
elif user =="paper" and computerchoice == "paper":
    print("its a tie!")
elif user =="scissors" and computerchoice == "rock":
    print("You lose!")
elif user =="scissors" and computerchoice == "paper":
    print("You win!")
elif user =="scissors" and computerchoice == "scissors":
    print("its a tie!")
else:
    print("write a valid: rock, paper, or scissors")

