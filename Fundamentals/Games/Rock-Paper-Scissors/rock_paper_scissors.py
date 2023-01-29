import random

list_of_choices = ["Rock", "Paper", "Scissors"]


while True:
    computer_choice = random.choice(list_of_choices)
    user_input = input(f"Please enter r - Rock, p - Paper or s - Scissors - ").lower()

    if user_input == "r":
        user_choice = "Rock"
    elif user_input == "p":
        user_choice = "Paper"
    elif user_input == "s":
        user_choice = "Scissors"
    else:
        print(f"Please enter correct letter")
        continue

    if user_choice == "Rock" and computer_choice == "Scissors" \
        or user_choice == "Paper" and computer_choice == "Rock" \
            or user_choice == "Scissors" and computer_choice == "Paper":
        print(f"Your choice is {user_choice} - {computer_choice} is computer choice")
        print("You WIN")
        break
    elif user_choice == computer_choice:
        print(f"Your choice is {user_choice} - {computer_choice} is computer choice")
        print("Draw")
        continue
    else:
        print(f"Your choice is {user_choice} - {computer_choice} is computer choice")
        print("You LOSE")
        break
