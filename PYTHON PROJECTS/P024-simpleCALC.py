def simple_calculator():
    """ A basic calculator for simple operations """

    name = input("Enter your name: ")
    print(f"Welcome, {name}! Let's calculate.")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

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
        else:
            print("Invalid operation")

        print("Result:", result)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    simple_calculator()
