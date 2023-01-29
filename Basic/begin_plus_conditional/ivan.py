from math import floor

world_record = float(input())
distance = float(input())
secs_for_one_meter = float(input())

water_resistance_seconds = floor(distance / 15) * 12.5
swimming_records = distance * secs_for_one_meter + water_resistance_seconds

if swimming_records > world_record:
    print(f"No, he failed! He was {swimming_records - world_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {swimming_records:.2f} seconds.")
