import random

while True:
    userInput = input("enter:\n'r' to roll the dice\n'q' to quit\n👉")

    if userInput == "q":
        print("Thanks for rolling!!!✌")
        break
    elif userInput == "r":
        print("🎲",random.randint(1,6))
    else:
        print("invalid input")

