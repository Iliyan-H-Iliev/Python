rows, cols = [int(x) for x in input().split()]

for i in range(ord("a"), ord("a") + rows):
    for j in range(cols):
        print(chr(i)+chr(i + j)+chr(i), end=" ")
    print()
