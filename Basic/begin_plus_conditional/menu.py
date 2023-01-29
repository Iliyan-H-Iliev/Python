number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegan_menu = int(input())


chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
delivery = 2.50

menus_total_price = \
    number_chicken_menu * chicken_menu + \
    number_fish_menu * fish_menu + \
    number_vegan_menu * vegan_menu

desert_price = menus_total_price * 0.2

total_price = menus_total_price + desert_price + delivery

print(total_price)
