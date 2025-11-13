import random #module

target  = random.randint(0,75)#to generate a random integer
moves = 0
while True:
    userChoice = input("guess the number or quit by pressing Q:")
    if(userChoice=="Q"):
        break
    else:
        userChoice = int(userChoice)
        if(userChoice==target):
            print("Success in",moves,"moves")
            break
        elif(userChoice>target):
            print("take a smaller guess")
            moves+=1
        else:
            print("take a bigger guess")
            moves+=1

print("---game over---")
    