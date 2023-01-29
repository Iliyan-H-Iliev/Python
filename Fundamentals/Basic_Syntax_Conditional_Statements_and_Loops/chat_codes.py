n = int(input())

for _ in range(0, n):
    command = int(input())

    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command > 88:
        print("Bye.")
    else:
        print("GREAT!")
