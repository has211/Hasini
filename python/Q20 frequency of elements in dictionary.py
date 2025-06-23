d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
freq = {}

for value in d.values():
    freq[value] = freq.get(value, 0) + 1

print("Frequency of values:", freq)
