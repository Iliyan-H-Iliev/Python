n = int(input())

student_grade = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in student_grade:
        student_grade[student_name] = []

    student_grade[student_name].append(grade)

for name, total_grade in student_grade.items():
    average_grade = sum(total_grade) / len(total_grade)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
