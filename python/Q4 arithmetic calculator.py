#Write a Python program to create a simple arithmetic calculator that takes two numbers and an operator (+, -, *, /) as input from the user and returns the result. Use separate functions for each operation, and ensure the program handles invalid operators and division by zero gracefully

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(add(a, b))
elif op == '-':
    print(sub(a, b))
elif op == '*':
    print(mul(a, b))
elif op == '/':
    print(div(a, b))
else:
    print("Invalid operator")
