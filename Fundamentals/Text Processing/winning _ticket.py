tickets = [x.strip() for x in input().split(",")]

winning_symbols = ['@', '#', '$', '^']

for el in tickets:

    if len(el) != 20:
        print("invalid ticket")
        continue

    first_half = el[:10]
    second_half = el[10:]
    is_win = False
    winning_element = ""

    for elm in winning_symbols:

        for i in range(6, 11):
            if elm * i in first_half and elm * i in second_half:
                winning_element = elm * i
                is_win = True
            else:
                break

    if is_win:
        if len(winning_element) == 10:
            print(f'ticket "{el}" - {len(winning_element)}{winning_element[0]} Jackpot!')
        else:
            print(f'ticket "{el}" - {len(winning_element)}{winning_element[0]}')
    else:
        print(f'ticket "{el}" - no match')
