def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    if operator == '+':
        print("Result =", a + b)
    elif operator == '-':
        print("Result =", a - b)
    elif operator == '*':
        print("Result =", a * b)
    elif operator == '/':
        print("Result =", a / b)
    else:
        print("Invalid operation")