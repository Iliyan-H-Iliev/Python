w = float(input())
h = float(input()) - 1

desk_w = w // 1.2
desk_h = h // 0.7

total_desks = (desk_h * desk_w) - 3

print(int(total_desks))
