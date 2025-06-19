# Number series
for i in range(1, 11):
    print(i**2, end=' ')

# Number pattern
rows = int(input("\nEnter number of rows for pattern: "))
for i in range(1, rows + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))

# Pyramid pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
