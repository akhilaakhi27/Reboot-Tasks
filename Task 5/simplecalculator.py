def calculator():
    operation = input("Choose operation (add, subtract, multiply, divide): ").lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == "add":
        print(f"The result is: {num1 + num2}")
    elif operation == "subtract":
        print(f"The result is: {num1 - num2}")
    elif operation == "multiply":
        print(f"The result is: {num1 * num2}")
    elif operation == "divide":
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation.")
calculator()
