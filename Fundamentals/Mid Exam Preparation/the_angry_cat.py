price_list = [int(x) for x in input().split(", ")]
entry_point = int(input())
item_pyte = input()

entry_point_price = price_list[entry_point]
left_side = price_list[:entry_point]
right_side = price_list[entry_point + 1:]

left_side_price = 0
right_side_price = 0

if item_pyte == "cheap":
    left_side_price = sum([x for x in left_side if x < entry_point_price])
    right_side_price = sum([x for x in right_side if x < entry_point_price])
elif item_pyte == "expensive":
    left_side_price = sum([x for x in left_side if x >= entry_point_price])
    right_side_price = sum([x for x in right_side if x >= entry_point_price])

if left_side_price >= right_side_price:
    print(f"Left - {left_side_price}")
else:
    print(f"Right - {right_side_price}")
