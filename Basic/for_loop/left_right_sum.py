num = int(input())

left_sum = 0
right_sum = 0

for _ in range(0, num):
    number = int(input())
    left_sum += number

for _ in range(0, num):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
