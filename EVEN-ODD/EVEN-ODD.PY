def even_odd_checker():
    while True:
        # Ask the user to enter a number
        user_input = input("\nEnter a number (or type 'exit' to quit): ")

        # Exit the program if the user types 'exit'
        if user_input.lower() == 'exit':
            print("🚀 Exiting the program. Goodbye! 🚀")
            break

        # Validate if the input is a number
        try:
            number = int(user_input)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        # Check if the number is even or odd
        if number % 2 == 0:
            print(f"🔢 {number} is an Even number.")
        else:
            print(f"🔢 {number} is an Odd number.")

# Run the program
even_odd_checker()