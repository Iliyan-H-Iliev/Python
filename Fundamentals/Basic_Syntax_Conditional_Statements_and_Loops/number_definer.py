number = float(input())

if number == 0:
    print("zero")
elif 0 < abs(number) < 1:
    if number > 0:
        print("small positive")
    else:
        print("small negative")
elif abs(number) > 1000000:
    if number > 0:
        print("large positive")
    else:
        print("large negative")
else:
    if number > 0:
        print("positive")
    else:
        print("negative")
