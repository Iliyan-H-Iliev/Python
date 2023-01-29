judge = int(input())

total_assessment = 0
count_assessment = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    sum_assessment = 0

    for i in range(0, judge):
        assessment = float(input())
        sum_assessment += assessment
        total_assessment += assessment
        count_assessment += 1

    print(f"{presentation_name} - {sum_assessment / judge:.2f}.")
print(f"Student's final assessment is {total_assessment / count_assessment:.2f}.")
