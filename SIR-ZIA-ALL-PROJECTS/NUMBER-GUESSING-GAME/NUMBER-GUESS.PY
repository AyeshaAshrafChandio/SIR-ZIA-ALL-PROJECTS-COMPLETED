import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        # Ask the user to guess the number
        try:
            guess = int(input("\nGuess the number: "))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
            return
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        # Display remaining attempts
        print(f"Attempts left: {max_attempts - attempts}")

    # If the user runs out of attempts
    print(f"\n😢 You've run out of attempts! The correct number was {secret_number}.")

# Run the game
number_guessing_game()