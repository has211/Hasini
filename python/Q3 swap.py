#Write a python program to swap the value of two variables (with temporary variable and without temporary variable)
# With temporary variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))
temp = a
a = b
b = temp
print("After swapping with temp:", a, b)

# Without temporary variable
a = int(input("Enter a again: "))
b = int(input("Enter b again: "))
a, b = b, a
print("After swapping without temp:", a, b)
