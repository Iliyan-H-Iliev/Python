deposit = float(input())
deposit_time = int(input())
rate = float(input()) / 100

rate_end = deposit * rate
montly_rate = rate_end / 12
end_of_deposit = deposit + deposit_time * montly_rate

print(end_of_deposit)
