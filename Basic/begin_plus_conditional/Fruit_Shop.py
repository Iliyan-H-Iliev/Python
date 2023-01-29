fruit = input()
day = input()
quantity = float(input())

price = 0
is_input = True

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == 'banana':
        price = quantity * 2.50
    elif fruit == 'apple':
        price = quantity * 1.2
    elif fruit == 'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.7
    elif fruit == 'pineapple':
        price = quantity * 5.5
    elif fruit == 'grapes':
        price = quantity * 3.85
    else:
        is_input = False
elif day == "Saturday" or day == "Sunday":
    if fruit == 'banana':
        price = quantity * 2.70
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit == 'orange':
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.6
    elif fruit == 'kiwi':
        price = quantity * 3
    elif fruit == 'pineapple':
        price = quantity * 5.6
    elif fruit == 'grapes':
        price = quantity * 4.2
    else:
        is_input = False
else:
    is_input = False

if is_input:
    print(f'{price:.2f}')
else:
    print('error')
