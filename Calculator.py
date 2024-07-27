import os

# Addition Function
def addition(num1, num2):
    return num1 + num2

# Subtraction Function
def subtraction(num1, num2):
    return num1 - num2

# Multiplication Function
def multiplication(num1, num2):
    return num1 * num2

# Division Function
def division(num1, num2):
    # Checking for 0 in denominator
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Attempt to divide by zero!"

# User Input Function
def get_user_input():
    # Validating input for numeric values
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please, enter numeric values only.")
        return get_user_input()

# Main Function
def main():
    while True:
        
         # Selection Prompts
        print("Welcome, select operation to continue")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        # Taking input for desired operation
        choice = input("Enter your choice: ")
        
        # Validating choices to get user input
        if choice in ('1', '2', '3', '4'):
            num1, num2 = get_user_input()

            # Calling function and printing output according to user's selected operation
            if choice == '1':
                print("Addition:")
                print(f"Result: {addition(num1, num2)}")
            elif choice == '2':
                print("Subtraction:")
                print(f"Result: {subtraction(num1, num2)}")
            elif choice == '3':
                print("Multiplication:")
                print(f"Result: {multiplication(num1, num2)}")
            elif choice == '4':
                print("Division:")
                print(f"Result: {division(num1, num2)}")
        elif choice == '5':
            #Clearing Screen
            os.system("CLS")
            print("Quitting... Good Bye!")
            break
        else:
            print("Invalid choice selection, retry.")
        
        #Checking If user want to exit or perform another calculation
        print("Do you want to perform another calculation?: ")
        next_calculation = input("Enter 'y' to confirm or Any other key to exit. ")
        #Clearing Screen
        os.system("CLS")
        if next_calculation.lower() != 'y':
            break

if __name__ == "__main__":
    main()
