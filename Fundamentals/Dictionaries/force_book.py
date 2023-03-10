force_book = {}

is_joint = False

while True:
    line = input()

    if line == "Lumpawaroo":
        break

    if "|" in line:
        force_side, force_user = line.split(" | ")
        if force_side not in force_book and force_user not in [x for v in force_book.values() for x in v]:
            force_book[force_side] = [force_user]
        elif force_user not in [x for v in force_book.values() for x in v]:
            force_book[force_side].append(force_user)

    elif " -> " in line:
        force_user, force_side = line.split(" -> ")
        if force_side not in force_book and force_user not in [x for v in force_book.values() for x in v]:
            force_book[force_side] = [force_user]
            is_joint = True
        elif force_user not in [x for v in force_book.values() for x in v]:
            force_book[force_side].append(force_user)
            is_joint = True
        elif force_user in [x for v in force_book.values() for x in v]:
            for k, v in force_book.items():
                if force_user in v:
                    force_book[k].remove(force_user)
            if force_side in force_book:
                force_book[force_side].append(force_user)
            else:
                force_book[force_side] = [force_user]
            is_joint = True

        if is_joint:
            print(f"{force_user} joins the {force_side} side!")

for k, v in force_book.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for el in v:
            print(f"! {el}")
