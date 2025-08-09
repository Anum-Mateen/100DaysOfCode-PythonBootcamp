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

computer_choice = random.randint(0,2)

print("WELCOME TO ROCK, PAPER, SCISSORS!")
user_choice = int(input("What do you choose? " 
                    "Type 0 for Rock, "
                    "1 for Paper "
                    "or 2 for Scissors.\n"))

print("You chose: \n", game_images[user_choice])

print("Computer chose: \n", game_images[computer_choice])

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose!")
elif game_images[user_choice] == rock and game_images[computer_choice] == scissors:
    print("You win!")
elif game_images[user_choice] == scissors and game_images[computer_choice] == rock:
    print("You lose!")
elif game_images[user_choice] == paper and game_images[computer_choice] == rock:
    print("You win!")
elif game_images[user_choice] == rock and game_images[computer_choice] == paper:
    print("You lose!")
elif game_images[user_choice] == scissors and game_images[computer_choice] == paper:
    print("You win!")
elif game_images[user_choice] == paper and game_images[computer_choice] == scissors:
    print("You lose!")
else:
    print("It is a draw!")