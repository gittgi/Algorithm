tc = int(input())
for test_case in range(tc):
    n = int(input())
    arr = [([0] * n)for _ in range(n)]

    i = 0                                   # i와 j의 시작 지점은 0,0
    j = 0
    num = 1                                 # 시작 숫자는 1
    arr[i][j] = num                         # 1을 쓰고 시작
    while j < n-1:                          # 끝에 닿기 전까지
        num += 1                            # 숫자를 올리고
        j += 1                              # j(열) 방향으로 한칸 옮기고
        arr[i][j] = num                     # 숫자 기록
    while i < n-1:                          # 끝에 닿으면 i로 똑같이 반복
        num += 1
        i += 1
        arr[i][j] = num
    while j > 0:                            # 마찬가지로 반복하되 역으로 이동
        num += 1
        j -= 1
        arr[i][j] = num
    while i > 1:
        num += 1
        i -= 1
        arr[i][j] = num                     # 같은 방식으로 1,0 까지만 이동

    while True:
        if num == n ** 2:                   # 마지막 수 (제곱) 에 도달하기 전까지
            break
        else:
            while arr[i][j+1] == 0:         # 다음칸이 비어있다면 (0이라면) 숫자 올리고 한칸 옮기고 기록하는 것을 반복
                num += 1
                j += 1
                arr[i][j] = num
            while arr[i+1][j] == 0:         # 비어있지 않으면 방향을 바꿔서 반복
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

