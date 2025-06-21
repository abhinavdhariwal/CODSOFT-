# Simple Calculator Program in Python
# Made by Abhinav (BTech ECE Student)

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operator selected."

        return f"The result is: {result}"

    except ValueError:
        return "Invalid input! Please enter numbers only."

# Run the calculator
print(calculator())