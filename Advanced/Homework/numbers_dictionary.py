all_numbers = {}

user_text = input()

while user_text != "Search":
    number_as_str = user_text

    try:
        number = int(input())
        all_numbers[number_as_str] = number
    except ValueError:
        print("The variable number must be an integer!")

    user_text = input()

user_text = input()

while user_text != "Remove":
    target_num = user_text

    try:
        print(all_numbers[target_num])
    except KeyError:
        print("Number does not exist in dictionary!")

    user_text = input()

user_text = input()

while user_text != "End":
    target_num = user_text

    try:
        del all_numbers[target_num]
    except KeyError:
        print("Number does not exist in dictionary!")

    user_text = input()

print(all_numbers)
