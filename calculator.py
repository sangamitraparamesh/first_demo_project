while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result =", a / b)

    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 5.")

