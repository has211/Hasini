#Write a Python program using simple statements and expressions (exchange the values of two variables, circulate the values of n variables and distance between two points)
# Exchange
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After exchange:", a, b)

# Circulate n variables
n = int(input("Enter number of variables: "))
values = []
for i in range(n):
    values.append(int(input(f"Enter value {i+1}: ")))
values = values[-1:] + values[:-1]
print("After circulation:", values)

# Distance between two points
import math
x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)
