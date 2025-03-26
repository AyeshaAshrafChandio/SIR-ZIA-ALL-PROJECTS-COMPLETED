import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define character sets based on user preferences
    characters = string.ascii_lowercase  # Always include lowercase letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("🔐 Welcome to the Password Generator! 🔐")

    while True:
        # Ask for password length
        try:
            length = int(input("\nEnter password length (minimum 8): "))
            if length < 8:
                print("❌ Password must be at least 8 characters long!")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            continue

        # Ask for character preferences
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")

        # Ask if the user wants to generate another password
        another = input("\nGenerate another password? (y/n): ").lower()
        if another != 'y':
            print("🚀 Thank you for using the Password Generator. Goodbye! 🚀")
            break

# Run the password generator
password_generator()
