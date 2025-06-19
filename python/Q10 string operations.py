#Implementing programs using Strings. (reverse, character count and replacing characters)

s = input("Enter a string: ")
# Reverse
print("Reversed:", s[::-1])
# Character count
print("Character count:", len(s))
# Replace characters
old = input("Character to replace: ")
new = input("Replace with: ")
print("Modified string:", s.replace(old, new))
