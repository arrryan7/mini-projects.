import random

choices = ["🥊","📃","✂"]

while True:
    userinput = input("Choose(enter) '🥊','📃','✂' or 'q' to quit\n")

    if userinput == "q":
        print("Thanks for playing✌")
        break

    if userinput not in choices:
        print("Invalid")

    comp_choice = random.choice(choices)
    if comp_choice == userinput:
        print("Draw")

    elif (comp_choice == "🥊" and userinput == "📃") or \
        (comp_choice == "📃" and userinput == "✂") or \
        (comp_choice == "✂" and userinput == "🥊"):
        print("You won🙌")

    else:
        print("You lost💀")
         
