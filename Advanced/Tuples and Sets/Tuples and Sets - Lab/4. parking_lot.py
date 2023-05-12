parking_lot = set()

for _ in range(int(input())):
    command, number_plate = input().split(", ")
    parking_lot.add(number_plate) if command == "IN" else parking_lot.remove(number_plate)
    # if command == "IN":
    #     parking_lot.add(number_plate)
    # elif command == "OUT":
    #     if number_plate in parking_lot:
    #         parking_lot.remove(number_plate)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")
