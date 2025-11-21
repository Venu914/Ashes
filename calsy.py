def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# New feature: Power function
def power(a, b):
    return a ** b

print("Simple Calculator")
print("Operations: +, -, *, /, ^")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /, ^): ")

if op == "+":
    print("Result =", add(a, b))
elif op == "-":
    print("Result =", subtract(a, b))
elif op == "*":
    print("Result =", multiply(a, b))
elif op == "/":
    print("Result =", divide(a, b))
elif op == "^":
    print("Result =", power(a, b))
else:
    print("Invalid Operation")
