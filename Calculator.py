# Simple Calculator Program

# Input two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input operation choice
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Invalid operation."

# Display the result
print("Result =", result)
