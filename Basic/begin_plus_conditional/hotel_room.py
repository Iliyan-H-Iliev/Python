month = input()
nights = int(input())

apartment_total_price = 0
studio_total_price = 0

if month == "May" or month == "October":
    apartment_total_price = nights * 65
    studio_total_price = nights * 50
    if 7 < nights <= 14:
        studio_total_price *= 0.95
    elif nights > 14:
        studio_total_price *= 0.70

elif month == "June" or month == "September":
    apartment_total_price = nights * 68.70
    studio_total_price = nights * 75.20
    if nights > 14:
        studio_total_price *= 0.8

elif month == "July" or month == "August":
    apartment_total_price = nights * 77
    studio_total_price = nights * 76

if nights > 14:
    apartment_total_price *= 0.9

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
