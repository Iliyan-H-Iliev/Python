input_list = list(input().split(" "))
terminated = False
result = []

[result.append(x) for x in input_list if x not in result]

team_a_counter = 11
team_b_counter = 11

for element in result:

    if element[0] == "A":
        team_a_counter -= 1
    elif element[0] == "B":
        team_b_counter -= 1

    if team_a_counter < 7 or team_b_counter < 7:
        terminated = True
        break

print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")

if terminated:
    print("Game was terminated")
