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

choice = int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
print(game_images[choice])

comp_choice = random.randint(0, 2)
print("Computer's choice")
print(game_images[comp_choice])

if choice >= 3 or choice < 0:
    print("You selected an invalid number. Game over.")
elif choice == 0 and comp_choice == 1:
    print("You won!!!")
elif comp_choice == 0 and choice == 1:
    print("You lost (-__-)")
elif comp_choice > choice:
    print("You lost (-__-)")
elif choice > comp_choice:
    print("You won!!!")
elif comp_choice == choice:
    print("It's a draw. Try again")
