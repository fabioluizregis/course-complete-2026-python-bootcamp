number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error: Division by zero"
    case _:
        result = "Error: Invalid operation"

print("The result is:", result)