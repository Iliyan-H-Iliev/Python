def largest_count(n, arr):
    rows = len(arr)
    cols = len(arr[0])
    max_count = 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == ".":
                count = nss(arr, i, j, rows, cols)
                max_count = max(max_count, count)
    return max_count


def nss(arr, i, j, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols or arr[i][j] != ".":
        return 0
    arr[i][j] = "#"
    count = 1
    count += nss(arr, i + 1, j, rows, cols)
    count += nss(arr, i - 1, j, rows, cols)
    count += nss(arr, i, j + 1, rows, cols)
    count += nss(arr, i, j - 1, rows, cols)
    return count


nnum = int(input().strip())
nic_lst = []
for i in range(nnum):
    row = input().strip().split()
    nic_lst.append(row)
print(largest_count(nnum, nic_lst))
