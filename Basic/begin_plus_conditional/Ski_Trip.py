days = int(input())
type_room = input()
rating = input()

total_room_price = 0

if type_room == "room for one person":
    total_room_price = (days - 1) * 18
    if rating == "positive":
        total_room_price *= 1.25
    elif rating == "negative":
        total_room_price *= 0.9

elif type_room == "apartment":
    total_room_price = (days - 1) * 25
    if days < 10:
        total_room_price *= 0.7
    elif 10 <= days <= 15:
        total_room_price *= 0.65
    elif days > 15:
        total_room_price *= 0.5

    if rating == "positive":
        total_room_price *= 1.25
    elif rating == "negative":
        total_room_price *= 0.9

elif type_room == "president apartment":
    total_room_price = (days - 1) * 35
    if days < 10:
        total_room_price *= 0.9
    elif 10 <= days <= 15:
        total_room_price *= 0.85
    elif days > 15:
        total_room_price *= 0.8

    if rating == "positive":
        total_room_price *= 1.25
    elif rating == "negative":
        total_room_price *= 0.9

print(f"{total_room_price:.2f}")
