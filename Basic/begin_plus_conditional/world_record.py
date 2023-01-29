from math import floor

world_record = float(input())
distance = float(input())
sec_for_meter = float(input())

water_resistance = floor(distance / 15) * 12.5
swimming_records = distance * sec_for_meter + water_resistance

if swimming_records >= world_record:
    print(f'No, he failed! He was {swimming_records - world_record:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {swimming_records:.2f} seconds.')
