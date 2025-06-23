positives = []
negatives = []

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

if positives:
    print("Average of positive numbers:", round(sum(positives)/len(positives), 2))
if negatives:
    print("Average of negative numbers:", round(sum(negatives)/len(negatives), 2))
