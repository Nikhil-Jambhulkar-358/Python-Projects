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
print = ("Welcome to Rock Paper Scissor Game")
user_input= int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissor. \n"))
# 0, 1, 2
print("You chose:")
print(game_images[user_input])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
elif user_input == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose!")
elif computer_choice > user_input:
    print("You Lose!")
elif computer_choice < user_input:
    print("You Win!")
elif computer_choice == user_input:
    print("It's a draw!")
