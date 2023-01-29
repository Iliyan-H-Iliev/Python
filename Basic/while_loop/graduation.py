name = input()

grade = 1
count = 0
total_average = 0

while True:
    average = float(input())

    if average < 4:
        count += 1
        if count >= 2:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue
    else:
        grade += 1

    total_average += average

    if grade > 12:
        print(f"{name} graduated. Average grade: {total_average / 12:.2f}")
        break
