import math

def advanced_calculator():
    """ A more advanced calculator with additional operations """

    name = input("Enter your name: ")
    print(f"Welcome, {name}! Let's calculate.")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /, ^, %, sqrt, log, sin, cos, tan): ")
        num2 = None

        if operator in ("+", "-", "*", "/", "^", "%"):
            num2 = float(input("Enter the second number: "))

        try:
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero")
                else:
                    result = num1 / num2
            elif operator == "^":
                result = num1 ** num2
            elif operator == "%":
                result = num1 % num2
            elif operator == "sqrt":
                result = math.sqrt(num1)
            elif operator == "log":
                result = math.log10(num1)
            elif operator == "sin":
                result = math.sin(math.radians(num1))
            elif operator == "cos":
                result = math.cos(math.radians(num1))
            elif operator == "tan":
                result = math.tan(math.radians(num1))
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid input")
        else:
            print("Result:", result)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    advanced_calculator()
