
# Mini Project: 8085 Microprocessor Arithmetic Calculator
# Subject: Computer Organization and Architecture

def display_menu():
    print("\n===== 8085 ARITHMETIC CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = int(input("Enter first number (0-255): "))
            num2 = int(input("Enter second number (0-255): "))

            if not (0 <= num1 <= 255 and 0 <= num2 <= 255):
                print("Please enter numbers between 0 and 255.")
                continue

            if choice == '1':
                result = num1 + num2
                print("Addition Result:", result)

            elif choice == '2':
                result = num1 - num2
                print("Subtraction Result:", result)

            elif choice == '3':
                result = num1 * num2
                print("Multiplication Result:", result)

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print("Division Result:", result)

        except ValueError:
            print("Invalid input! Please enter integers.")


if __name__ == "__main__":
    main()
