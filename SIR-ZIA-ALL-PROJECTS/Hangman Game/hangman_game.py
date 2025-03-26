import random

def hangman():
    # List of words to choose from
    words = ["apple", "banana", "python", "computer", "keyboard", "programming"]
    
    # Select a random word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Number of allowed wrong guesses
    
    print("🌟 Welcome to Hangman! 🌟")
    print(f"Guess the word. You have {attempts} wrong attempts allowed.")
    
    while attempts > 0:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: " + display_word)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if single letter was entered
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
        
        # Check if player won
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            return
    
    # If player runs out of attempts
    print(f"\n😢 Game Over! The word was: {secret_word}")

# Start the game
hangman()