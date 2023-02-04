def data_types(types, a):
    result = None
    if types == "int":
        result = int(a) * 2
    elif types == "real":
        result = f"{(float(a) * 1.5):.2f}"
    elif types == "string":
        result = "$"+a+"$"
    return result


type_input = input()
string_input = input()

print(data_types(type_input, string_input))
