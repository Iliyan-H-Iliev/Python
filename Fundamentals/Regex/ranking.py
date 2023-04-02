contest_list = {}
submissions_list = {}
best_candidate = ""
best_points = 0

while True:
    contest_and_password = input()

    if contest_and_password == "end of contests":
        break

    contest_and_password_args = contest_and_password.split(":")
    contest = contest_and_password_args[0]
    password = contest_and_password_args[1]
    if contest not in contest_list:
        contest_list[contest] = password

while True:
    data = input()

    if data == "end of submissions":
        break

    data_args = data.split("=>")
    contest = data_args[0]
    password = data_args[1]
    name = data_args[2]
    points = int(data_args[3])

    if contest not in contest_list:
        continue

    if contest_list[contest] == password:

        if name not in submissions_list:
            submissions_list[name] = {contest: points}
        else:
            if contest not in submissions_list[name]:
                submissions_list[name][contest] = points
            else:
                submissions_list[name][contest] = max(submissions_list[name][contest], points)


for k in submissions_list.keys():
    total_points = 0

    for x in submissions_list[k].keys():
        total_points += submissions_list[k][x]

    if total_points > best_points:
        best_candidate = k
        best_points = total_points

print(f"Best candidate is {best_candidate} with total {best_points} points.")
print("Ranking:")

sorted_by_name = sorted(submissions_list.keys(), key=lambda n: n[0])

for k in sorted_by_name:
    print(k)
    sorted_by_points = sorted(submissions_list[k].items(), key=lambda t: -t[1])
    for el in sorted_by_points:
        print(f"#  {el[0]} -> {el[1]}")
