def loading_bar(percent):
    result = ["."] * 10
    for i in range(percent // 10):
        result[i] = "%"
    return result

# def print_result(percent):


numb = int(input())

if 0 <= numb <= 99:
    print(f"{numb}% " + "[" + "".join(loading_bar(numb)) + "]")
    print("Still loading...")
elif numb == 100:
    print(f"{numb}% Complete!")
    print("[" + "".join(loading_bar(numb)) + "]")
