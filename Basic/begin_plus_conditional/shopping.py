budget = float(input())

count_video_cards = int(input())
count_processors = int(input())
count_rams = int(input())

price_video_card = 250
price_processor = price_video_card * count_video_cards * 0.35
price_ram = price_video_card * count_video_cards * 0.1

total_price = count_video_cards * price_video_card + \
    count_processors * price_processor + count_rams * price_ram

if count_video_cards > count_processors:
    total_price *= 0.85

if budget >= total_price:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')
