n = int(input())

cars = {}

for _ in range(n):
    data = input()
    car_args = data.split("|")
    car = car_args[0]
    mileage = car_args[1]
    fuel = car_args[2]

    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    data = input()

    if data == "Stop":
        break

    command_args = data.split(" : ")
    command = command_args[0]
    car = command_args[1]

    if command == "Drive":
        distance = int(command_args[2])
        fuel = int(command_args[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")

        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel = int(command_args[2])
        needed_fuel = 75 - cars[car]["fuel"]
        cars[car]["fuel"] = min(cars[car]["fuel"] + fuel, 75)
        print(f"{car} refueled with {min(fuel, needed_fuel)} liters")

    elif command == "Revert":
        kilometers = int(command_args[2])

        if cars[car]["mileage"] - kilometers >= 10000:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]["mileage"] = 10000

for car in cars.keys():
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
