distances_to_the_pokemon = [int(x) for x in input().split()]
counter = 0
while distances_to_the_pokemon:
    index = int(input())


    if index < 0:
        removed_element = distances_to_the_pokemon[0]
        counter += removed_element
        distances_to_the_pokemon[0] = distances_to_the_pokemon[-1]
    elif index >= len(distances_to_the_pokemon):
        removed_element = distances_to_the_pokemon[-1]
        counter += removed_element
        distances_to_the_pokemon[-1] = distances_to_the_pokemon[0]
    else:
        removed_element = distances_to_the_pokemon[index]
        counter += removed_element
        distances_to_the_pokemon.pop(index)

    distances_to_the_pokemon = [el + removed_element if el <= removed_element else el - removed_element \
                                    for el in distances_to_the_pokemon]

print(counter)
