class Adventure_game:
    def __init__(self):
        print("Welcome to the game!!!")
        print("You find yourself at a crossroads in a dense forest.")
    
    def start(self):
        print("1.Enter the dark cave.")
        print("2.Follow the path through the forest.")
        choice = input("What do you want to do?")
        
        if choice == '1':
            self.enter_cave()
        elif choice == '2':
            self.follow_path()
        else:
            print("\nInvalid choice. Adventure ends here.")

    def enter_cave(self):
        print("\nInside the cave, you find a treasure chest.")
        print("1.Open the chest.")
        print("2.Leave the cave.")
        choice = input("What do you want to do?")
        if choice == '1':
            print("\nYou found a valuable gem!!!")
        elif choice == '2':
            print("\nYou leave the cave safely.")
        else:
            print("\nInvalid choice. Adventure ends here.")

    def follow_path(self):
        print("\nThe path splits into two directions.")
        print("1.Take left.")
        print("2.Take right.")
        choice = input("What do you want to do?")
        if choice == '1':
            print("\nYou discovered a hidden waterfall.")
        elif choice == '2':
            print("\nThe path leads to a dead end.")
        else:
            print("\nInvalid choice. Adventure ends here.")

game = Adventure_game()
game.start()            