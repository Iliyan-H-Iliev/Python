students = {}

for _ in range(int(input())):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for name, grade in students.items():
    avg = sum(grade) / len(grade)

    print(f"{name} -> {' '.join(str(f'{x:.2f}') for x in grade)} (avg: {avg:.2f})")
