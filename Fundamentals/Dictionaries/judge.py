contest_dict = {}
students = {}

while True:
    line = input().split(" -> ")

    if line[0] == "no more time":
        break

    name = line[0]
    contest = line[1]
    points = int(line[2])

    if contest not in contest_dict:
        contest_dict[contest] = {name: points}
        if name not in students:
            students[name] = points
        else:
            students[name] += points
    else:
        if name not in contest_dict[contest]:
            contest_dict[contest][name] = points
            if name not in students:
                students[name] = points
            else:
                students[name] += points
        else:
            if contest_dict[contest][name] < points:
                students[name] += points - contest_dict[contest][name]
                contest_dict[contest][name] = points

for k, v in contest_dict.items():
    print(f"{k}: {len(v)} participants")
    sorted_value = sorted(v.items(), key=lambda x: (-x[1], x[0]))
    for i in range(len(sorted_value)):
        print(f"{i + 1}. {sorted_value[i][0]} <::> {sorted_value[i][1]}")

print("Individual standings:")
sorted_names = sorted(students.items(), key=lambda x: (-x[1], x[0]))
for i in range(len(sorted_names)):
    print(f"{i + 1}. {sorted_names[i][0]} -> {sorted_names[i][1]}")
