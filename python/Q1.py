#A shopkeeper wants to calculate the total bill for a customer. The shopkeeper has a list of items, where each item has a price and quantity. Write a program to calculate the total cost using appropriate data types

s = input("Enter a string: ")
# Reverse
print("Reversed:", s[::-1])
# Character count
print("Character count:", len(s))
# Replace characters
old = input("Character to replace: ")
new = input("Replace with: ")
print("Modified string:", s.replace(old, new))
