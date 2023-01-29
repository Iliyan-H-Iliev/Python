price_skumriq = float(input())
price_caca = float(input())
weight_palamud = float(input())
weight_safrid = float(input())
weight_midi = int(input())

price_palamud = price_skumriq + price_skumriq * 0.6
price_safrid = price_caca + price_caca * 0.8
price_midi = 7.5

total_price =\
    price_palamud * weight_palamud + \
    price_safrid * weight_safrid + \
    price_midi * weight_midi

print(f'{total_price:.2f}')
