import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", math.gcd(a, b))
lcm = abs(a * b) // math.gcd(a, b)
print("LCM:", lcm)
