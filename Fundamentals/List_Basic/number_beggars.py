input_list = list(input().split(", "))
beggars = int(input())

int_list = [int(s) for s in input_list]
new_list = [0] * beggars

for i in range(len(int_list)):
    current_beggars = i % beggars
    new_list[current_beggars] += int_list[i]

print(new_list)
