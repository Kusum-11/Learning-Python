# Guess the number
import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit the game(press Q for Quit)")
    if userChoice == "Q":
        break
    userChoice = int(userChoice)
    if userChoice == target:
        print("Success : Correct Guess!")
        break
    elif userChoice < target:
        print("Guess number is less than target number. \nGuess again...")
    else:
        print("Guess number is greater than target number. \nGuess again...")

print("----GAME OVER----")