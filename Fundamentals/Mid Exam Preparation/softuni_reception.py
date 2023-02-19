person_1 = int(input())
person_2 = int(input())
person_3 = int(input())

answer_per_hour = person_1 + person_2 + person_3
hours = 0

student_count = int(input())

while student_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue

    student_count -= min(answer_per_hour, student_count)

print(f"Time needed: {hours}h.")
