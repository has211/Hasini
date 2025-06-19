#Implementing programs using Functions. (Factorial, largest number in a list and area of shape)
# Factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print("Factorial:", factorial(int(input("Enter number: "))))

# Largest number
lst = list(map(int, input("Enter list elements: ").split()))
print("Largest:", max(lst))

# Area of shape (circle)
import math
radius = float(input("Enter radius: "))
print("Area of circle:", math.pi * radius * radius)
