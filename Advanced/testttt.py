# Read the size of the field 
size = int(input())

# Read the field matrix
field = []
for _ in range(size):
    row = input().split()
    field.append(row)

    # Define the possible directions
directions = ["up", "down", "left", "right"]


# collect eggs and calculate the total number of eggs
def collect_eggs(field, direction):
    rows = len(field)
    cols = len(field[0])
    collected_eggs = []
    total_eggs = 0

    if direction == "up":
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == "B":
                    bunny_row = row
                    bunny_col = col
                    break
            else:
                continue
            break

        for row in range(bunny_row - 1, -1, -1):
            if field[row][bunny_col] == "X":
                break
            elif field[row][bunny_col] != 0:
                collected_eggs.append([row, bunny_col])
                total_eggs += int(field[row][bunny_col])


    elif direction == "down":
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == "B":
                    bunny_row = row
                    bunny_col = col
                    break
            else:
                continue
            break

        for row in range(bunny_row + 1, rows):
            if field[row][bunny_col] == "X":
                break
            elif field[row][bunny_col] != 0:
                collected_eggs.append([row, bunny_col])
                total_eggs += int(field[row][bunny_col])


    elif direction == "left":
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == "B":
                    bunny_row = row
                    bunny_col = col
                    break
            else:
                continue
            break

        for col in range(bunny_col - 1, -1, -1):
            if field[bunny_row][col] == "X":
                break
            elif field[bunny_row][col] != 0:
                collected_eggs.append([bunny_row, col])
                total_eggs += int(field[bunny_row][col])


    elif direction == "right":
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == "B":
                    bunny_row = row
                    bunny_col = col
                    break
            else:
                continue
            break

        for col in range(bunny_col + 1, cols):
            if field[bunny_row][col] == "X":
                break
            elif field[bunny_row][col] != 0:
                collected_eggs.append([bunny_row, col])
                total_eggs += int(field[bunny_row][col])

    return collected_eggs, total_eggs

    # Convert "X" to 0 in the field matrix


for row in field:
    for i in range(len(row)):
        if row[i] == "X":
            row[i] = 0
        else:
            row[i] = int(row[i])

            # Define the possible directions
directions = ["up", "down", "left", "right"]

# Variables to keep track of the best direction and its result
best_direction = ""
best_collected_eggs = []
best_total_eggs = float("-inf")

# Iterate over each direction
for direction in directions:
    collected_eggs, total_eggs = collect_eggs(field, direction)

    # Check if this direction results in more eggs collected
    if total_eggs > best_total_eggs:
        best_direction = direction
        best_collected_eggs = collected_eggs
        best_total_eggs = total_eggs

        # Print the best direction, collected eggs positions, and total number of eggs collected
print(best_direction)
for position in best_collected_eggs:
    print(position[0], position[1])
print(best_total_eggs)