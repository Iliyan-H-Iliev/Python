employees_happiness = [int(x) for x in input().split()]
factor = int(input())

happiness = [x * factor for x in employees_happiness]
middle_factor = sum(happiness) / len(employees_happiness)
happy_people = [x for x in happiness if x >= middle_factor]

if len(happy_people) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_people)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(employees_happiness)}. Employees are not happy!")
