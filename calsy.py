import math

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

# Power function
def power(a, b):
    return a ** b

# Square root function
def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of a negative number"
    return math.sqrt(a)

print("Simple Calculator")
print("Operations: +, -, *, /, ^, sqrt")

a = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /, ^, sqrt): ")

# sqrt takes only one number, so ask for b only if needed
if op != "sqrt":
    b = float(input("Enter second number: "))

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
elif op == "sqrt":
    print("Result =", square_root(a))
else:
    print("Invalid Operation")
