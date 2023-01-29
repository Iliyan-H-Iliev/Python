pens = int(input())
markers = int(input())
cleaner = int(input())
discount_percent = int(input()) / 100

pen_price = 5.8
marker_price = 7.2
cleaner_price = 1.2

price_before_discount = (pens * pen_price) + (markers * marker_price) + (cleaner * cleaner_price)
discount = price_before_discount * discount_percent
total_price = price_before_discount - discount

print(total_price)
