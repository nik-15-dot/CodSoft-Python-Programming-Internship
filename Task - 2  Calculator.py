# Task - 2 : Calculator
#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
def calculator():
    # Prompt the user to enter the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Select operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    
    # Prompt the user to enter the operation choice
    option = input("Enter choice (a/b/c/d): ")
    
    # Perform the calculation based on the user's choice
    if option == 'a':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    elif option == 'b':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    elif option == 'c':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    elif option == 'd':
        if num2 != 0:  # Check to prevent division by zero
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input! Please select a valid operation.")

# Call the calculator function to run the program
calculator()