tc = int(input())
for test_case in range(tc):
    n = int(input())
    arr = [([0] * n)for _ in range(n)]

    i = 0
    j = 0
    num = 1
    arr[i][j] = num
    while j < n-1:
        num += 1
        j += 1
        arr[i][j] = num
    while i < n-1:
        num += 1
        i += 1
        arr[i][j] = num
    while j > 0:
        num += 1
        j -= 1
        arr[i][j] = num
    while i > 1:
        num += 1
        i -= 1
        arr[i][j] = num

    while True:
        if num == n ** 2:
            break
        else:
            while arr[i][j+1] == 0:
                num += 1
                j += 1
                arr[i][j] = num
            while arr[i+1][j] == 0:
                num += 1
                i += 1
                arr[i][j] = num
            while arr[i][j-1] == 0:
                num += 1
                j -= 1
                arr[i][j] = num
            while arr[i-1][j] == 0:
                num += 1
                i -= 1
                arr[i][j] = num
    print(f'#{test_case + 1}')
    for i in arr:
        print(*i)

