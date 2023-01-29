screening_type = input()
row = int(input())
columns = int(input())

income = 0

seats = row * columns

if screening_type == "Premiere":
    income = seats * 12
elif screening_type == "Normal":
    income = seats * 7.5
elif screening_type == "Discount":
    income = seats * 5

print(f'{income:.2f} leva')
