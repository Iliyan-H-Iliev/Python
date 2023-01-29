is_sorted = True

while True:
    name = input()

    if name == "Welcome!":
        break
    if name == "Voldemort":
        is_sorted = False
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if is_sorted:
    print("Welcome to Hogwarts.")
else:
    print("You must not speak of that name!" )
