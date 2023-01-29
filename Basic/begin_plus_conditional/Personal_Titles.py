age = float(input())
sex = input()

if sex == "f":
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
elif sex == "m":
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
