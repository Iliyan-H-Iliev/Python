parcel_weight = float(input())
service = input()
distance = int(input())

price_per_kilometer = 0
overprice = 0

if parcel_weight < 1:
    price_per_kilometer = 0.03
elif 1 <= parcel_weight < 10:
    price_per_kilometer = 0.05
elif 10 <= parcel_weight < 40:
    price_per_kilometer = 0.1
elif 40 <= parcel_weight < 90:
    price_per_kilometer = 0.15
else:
    price_per_kilometer = 0.2

if service == "express":
    if parcel_weight < 1:
        overprice = price_per_kilometer * 0.8
    elif 1 <= parcel_weight < 10:
        overprice = price_per_kilometer * 0.4
    elif 10 <= parcel_weight < 40:
        overprice = price_per_kilometer * 0.05
    elif 40 <= parcel_weight < 90:
        overprice = price_per_kilometer * 0.02
    else:
        overprice = price_per_kilometer * 0.01

total_price = (distance * price_per_kilometer) + (distance * (parcel_weight * overprice))

print(f"The delivery of your shipment with weight of {parcel_weight:.3f} kg. would cost {total_price:.2f} lv.")
