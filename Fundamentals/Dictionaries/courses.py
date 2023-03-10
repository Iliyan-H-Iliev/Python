courses_list = {}

while True:
    line = input()

    if line == "end":
        break

    course, student = line.split(" : ")

    if course not in courses_list:
        courses_list[course] = [student]
    else:
        courses_list[course].append(student)

for cour, stud in courses_list.items():
    print(f"{cour}: {len(stud)}")
    for name in stud:
        print(f"-- {name}")
