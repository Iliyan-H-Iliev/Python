company_users = {}

while True:
    line = input()

    if line == "End":
        break

    company, user_id = line.split(" -> ")

    if company not in company_users:
        company_users[company] = []

    if user_id not in company_users[company]:
        company_users[company].append(user_id)

for comp, users in company_users.items():
    print(comp)
    for el in users:
        print(f"-- {el}")
