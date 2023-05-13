n, m = input().split()

set_1 = {int(input()) for _ in range(int(n))}
set_2 = {int(input()) for _ in range(int(m))}

print(*set_1.intersection(set_2), sep="\n")
