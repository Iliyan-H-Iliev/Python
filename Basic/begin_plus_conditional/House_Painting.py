x = float(input())
y = float(input())
h = float(input())

front_wall = (x * x) - (1.2 * 2)
rear_wall = x * x
side_walls = ((x * y) - (1.5 * 1.5))

roof_triangles = (x * h) / 2
roof_walls = x * y

green_paint_walls = front_wall + rear_wall + (side_walls * 2)
red_paint_walls = (roof_triangles * 2) + (roof_walls * 2)

green_paint = green_paint_walls / 3.4
red_paint = red_paint_walls / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
