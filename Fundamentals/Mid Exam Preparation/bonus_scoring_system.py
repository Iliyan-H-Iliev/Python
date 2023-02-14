import math
from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus = 0
student_attendance = 0

for _ in range(students):
    attendances = int(input())

    if lectures != 0:
        total_bonus = ceil((attendances / lectures) * (5 + bonus))

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            student_attendance = attendances

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {student_attendance} lectures.")
