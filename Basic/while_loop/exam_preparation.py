unsatisfactory = int(input())

count_problems = 0
last_problem = ''
count_unsatisfactory = 0
total_score = 0

while unsatisfactory > count_unsatisfactory:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {total_score / count_problems:.2f}")
        print(f"Number of problems: {count_problems}")
        print(f"Last problem: {last_problem}")
        break

    last_problem = problem_name

    score = int(input())

    if score <= 4:
        count_unsatisfactory += 1

    count_problems += 1
    total_score += score

else:
    print(f"You need a break, {count_unsatisfactory} poor grades.")
