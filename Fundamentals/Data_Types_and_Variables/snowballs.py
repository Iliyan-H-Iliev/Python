n = int(input())
best_snowball = 0

snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for _ in range(n):
    current_snowball_weight = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball = (current_snowball_weight / current_snowball_time) ** current_snowball_quality

    if best_snowball < current_snowball:
        best_snowball = current_snowball
        snowball_weight = current_snowball_weight
        snowball_time = current_snowball_time
        snowball_quality = current_snowball_quality

print(f"{snowball_weight} : {snowball_time} = {int(best_snowball)} ({snowball_quality})")
