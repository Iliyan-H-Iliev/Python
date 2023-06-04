movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

start_position = [1, 1]


print(movement["down"][0])
print(movement["down"][1])
new_position = [
        (start_position[0] + movement["up"][0]),
        (start_position[1] + movement["up"][1]),
]

print(new_position)