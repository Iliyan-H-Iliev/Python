a = int(input())
b = int(input())
new_list = []
for i in range(1, b * a + 1):
    if i % a == 0:
        new_list.append(i)

print(new_list)
