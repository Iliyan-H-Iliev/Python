population_by_city = {}
gold_by_city = {}

while True:
    city_arg = input()

    if city_arg == "Sail":
        break

    city_args = city_arg.split("||")
    city = city_args[0]
    population = int(city_args[1])
    gold = int(city_args[2])

    if city not in population_by_city:
        population_by_city[city] = population
        gold_by_city[city] = gold
    else:
        population_by_city[city] += population
        gold_by_city[city] += gold

while True:
    command_intput = input()

    if command_intput == "End":
        break

    command_args = command_intput.split("=>")
    command = command_args[0]
    city = command_args[1]

    if command == "Plunder":
        people = int(command_args[2])
        gold = int(command_args[3])

        population_by_city[city] -= people
        gold_by_city[city] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if population_by_city[city] == 0 or gold_by_city[city] == 0:
            population_by_city.pop(city)
            gold_by_city.pop(city)
            print(f"{city} has been wiped off the map!")


    elif command == "Prosper":
        gold = int(command_args[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue

        gold_by_city[city] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {gold_by_city[city]} gold.")

if population_by_city:
    print(f"Ahoy, Captain! There are {len(population_by_city)} wealthy settlements to go to:")
    for city in population_by_city.keys():
        print(f"{city} -> Population: {population_by_city[city]} citizens, Gold: {gold_by_city[city]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
