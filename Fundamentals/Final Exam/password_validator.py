import string
password = input()

match = string.ascii_letters + string.digits + "_"

while True:
    data = input().split()
    command = data[0]

    if command == "Complete":
        break

    if command == "Make":
        command = f"{data[0]} {data[1]}"

    if command == "Make Upper":
        index = int(data[2])
        replace_index = password[index].upper()
        password = password[:index] + replace_index + password[index + 1:]
        print(password)
    elif command == "Make Lower":
        index = int(data[2])
        replace_index = password[index].lower()
        password = password[:index] + replace_index + password[index + 1:]
        print(password)
    elif command == "Insert":
        index = int(data[1])
        value = data[2]

        if 0 > index > len(password) - 1:
            continue

        password = password[:index] + value + password[index:]
        print(password)
    elif command == "Replace":
        char = data[1]
        value = int(data[2])

        if char not in password:
            continue

        new_char = chr(ord(char) + value)
        password = password.replace(char, new_char)
        print(password)
    elif command == "Validation":
        is_correct = True
        is_upper = False
        is_lower = False
        is_digit = False
        if len(password) < 8:
            print("Password must be at least 8 characters long!")

        for el in password:
            if not all([x in match for x in el]):
                is_correct = False
            if el.isupper():
                is_upper = True
            if el.islower():
                is_lower = True
            if el.isdigit():
                is_digit = True

        if not is_correct:
            print("Password must consist only of letters, digits and _!")
        if not is_upper:
            print("Password must consist at least one uppercase letter!")
        if not is_lower:
            print("Password must consist at least one lowercase letter!")
        if not is_digit:
            print("Password must consist at least one digit!")
