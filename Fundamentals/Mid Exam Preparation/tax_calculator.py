taxed_vehicles = input().split(">>")

total_tax = 0

for vehicle in taxed_vehicles:
    vehicle_arg = vehicle.split()
    vehicle_type = vehicle_arg[0]
    years = int(vehicle_arg[1])
    kilometers = int(vehicle_arg[2])

    tax_to_pay = 0

    if vehicle_type == "family":
        tax_to_pay += (50 - (years * 5)) + ((kilometers // 3000) * 12)
        total_tax += tax_to_pay
        print(f"A {vehicle_type} car will pay {tax_to_pay:.2f} euros in taxes.")

    elif vehicle_type == "heavyDuty":
        tax_to_pay = (80 - (years * 8)) + ((kilometers // 9000) * 14)
        total_tax += tax_to_pay
        print(f"A {vehicle_type} car will pay {tax_to_pay:.2f} euros in taxes.")

    elif vehicle_type == "sports":
        tax_to_pay = (100 - (years * 9)) + ((kilometers // 2000) * 18)
        total_tax += tax_to_pay
        print(f"A {vehicle_type} car will pay {tax_to_pay:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
