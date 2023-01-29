import math
movie_name = input()
movie_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
res_time = break_time / 4

total_time = movie_time + lunch_time + res_time
left_time = break_time - total_time

if left_time >= 0:
    print(f'You have enough time to watch {movie_name} and left with {math.ceil(left_time)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {movie_name}, you need {math.ceil(abs(left_time))} more minutes.')
