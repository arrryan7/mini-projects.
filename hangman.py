import random 

movies = ["interstellar", "wanted", "parasite", "train to busan", "mission impossible", "sanju", "animal",
          "interception", "kill bill", "the kissing booth", "jai ho", "twilight", "american pie", "the kashmir files",
          "the hangover"]

while True:
    choice = int(input("Enter 1 to START or 2 to QUIT:"))
    if choice == 2:
        print("BYE")
        break
    elif choice == 1:
        movie = random.choice(movies)
        lives = 7

        guessed = set()
        displayed = ''.join([c if c == ' ' else '_' for c in movie])
        
        while lives > 0 and '_' in displayed:
            print("\nMovie: ",''.join(displayed))
            print("Lives left:",lives)
            guess = input("guess a letter:").lower()

            if not guess or len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please guess a single letter.")
                continue

            if guess in guessed:
                print("You already guessed that letter.")
                continue
            guessed.add(guess)

            if guess in movie:
                displayed = ''.join([c if (c == ' ') or (c in guessed) else '_' for c in movie])
                print("Correct!")
            
            else:
                lives -= 1
                print("Wrong!")

        if '_' not in displayed:
            print("\nCongrats! You guessed the movie: ",movie)
        
        else:
            print("\nYou ran out of lives! The movie was:", movie)










   
    
    
