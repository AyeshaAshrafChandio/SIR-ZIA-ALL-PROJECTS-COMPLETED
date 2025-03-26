def smart_arithmetic_calculator():
    while True:
        # Display the operation menu
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Take user input for operation choice
        choice = input("Enter choice (1-5): ")

        # Exit the program if the user chooses 5
        if choice == '5':
            print("🚀 Exiting the calculator. Goodbye! 🚀")
            break

        # Validate the choice
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice! Please select a valid option (1-4).")
            continue

        # Take input for two numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                print("❌ Division by zero is not allowed!")
                continue
            result = num1 / num2
            operation = "/"

        # Round the result to 2 decimal places
        result_rounded = round(result, 2)

        # Display the result
        print(f"\n🧮 Calculating...")
        print(f"{num1} {operation} {num2} = {result_rounded}\n")

# Run the calculator
smart_arithmetic_calculator()
