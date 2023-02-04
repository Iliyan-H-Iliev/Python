def tribonacci(n):
    result = [1] * n
    if n <= 2:
        return result
    for i in range(2, n):
        if i == 2:
            result[i] = 2
            continue
        result[i] = result[i - 1] + result[i - 2] + result[i - 3]
    return result


numb = int(input())

for el in tribonacci(numb):
    print(el, end=" ")
