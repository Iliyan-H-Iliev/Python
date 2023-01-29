n = int(input())

positives_numbers = []
negatives_number = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positives_numbers.append(number)
    else:
        negatives_number.append(number)

print(positives_numbers)
print(negatives_number)
print(f"Count of positives: {len(positives_numbers)}\n"
      f"Sum of negatives: {sum(negatives_number)}")
