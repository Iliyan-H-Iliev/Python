import random

computer_number = 0
numbers_between = ""

print()
print("Guess A Number".center(95))
print()
print("1 - Easy (1 - 10);  2 - Normal (1 - 100);  3 - Hard (1 - 1000);  4 - Very Hard (1 - 10000)")
print()

while True:

    select_game_difficulty = input("Select Game Difficulty - ")

    if select_game_difficulty == "1":
        computer_number = random.randint(1, 10)
        numbers_between = "1 and 10"
        break
    elif select_game_difficulty == "2":
        computer_number = random.randint(1, 100)
        numbers_between = "1 and 100"
        break
    elif select_game_difficulty == "3":
        computer_number = random.randint(1, 1000)
        numbers_between = "1 and 1000"
        break
    elif select_game_difficulty == "4":
        computer_number = random.randint(1, 10000)
        numbers_between = "1 and 10000"
        break
    else:
        print("Please select correct number")

print()
print(f"You chose to play with numbers between {numbers_between}")
print()

while True:
    user_input = input(f"Guess a number: ")
    if not user_input.isdigit():
        print(f"Invalid input. Please choose a number between {numbers_between} ")
        continue

    if int(user_input) == computer_number:
        print("You WIN")
        break
    elif int(user_input) < computer_number:
        print("Too Low!")
    else:
        print("Too High!")
