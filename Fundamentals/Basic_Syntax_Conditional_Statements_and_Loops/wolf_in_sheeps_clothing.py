input_string = input()
list_from_string = input_string.split(", ")
list_from_string.reverse()

index = list_from_string.index("wolf")

if index == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
