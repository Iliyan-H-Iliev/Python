clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 0
clothes_count = 0

while clothes:
    current_clothes = clothes.pop()

    if clothes_count + current_clothes > rack_capacity:
        rack_count += 1
        clothes_count = current_clothes
    elif clothes_count + current_clothes < rack_capacity:
        clothes_count += current_clothes
    else:
        rack_count += 1
        clothes_count = 0

if clothes_count > 0:
    rack_count += 1

print(rack_count)
