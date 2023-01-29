divisor = int(input())
boundary = int(input())
n = 0

for i in range(divisor, boundary + 1):
    if i % divisor == 0 and 0 < i <= boundary:
        n = i

print(n)
