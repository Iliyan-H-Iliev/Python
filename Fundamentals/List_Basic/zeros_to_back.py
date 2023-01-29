input_list = list(input().split(", "))
new_list = []
zero_list = []


for i in input_list:

    if int(i) == 0:
        zero_list.append(0)
    else:
        new_list.append(int(i))

new_list += zero_list

print(new_list)
