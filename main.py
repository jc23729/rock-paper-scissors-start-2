import random


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
game_images = [rock, paper, scissors]

user_choice= int(input("What would you like to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if user_choice>=3  or user_choice <0:
  print("You chose an invalid numbe, YOU LOSE")
else:
  print(game_images[user_choice])

  computer_choice= random.randint(0,2)
  print("Computer chose:")
  print(game_images[computer_choice])
  # this choice will take care of everything out range out of 0-2 

  if user_choice == 0 and computer_choice == 2:
    print("You win")
  elif computer_choice ==0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win")
  elif computer_choice == user_choice:
    print("Its a draw")
