input_numbers = list(input().split())
n = int(input())

sort_list = [int(s) for s in input_numbers]
sort_list.sort()

for i in range(n):
    input_numbers.remove(str(sort_list[i]))

print(", ".join(input_numbers))
