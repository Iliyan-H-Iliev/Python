import random

random_number = random.randint(1, 100)

while True:
    num = int(input())

    if num == random_number:
        print("good")
        break
    elif num < random_number:
        print("up")
    else:
        print("down")

print(f"your number is {random_number}")
