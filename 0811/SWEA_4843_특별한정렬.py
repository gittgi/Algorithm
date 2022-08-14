tc = int(input())

for test_case in range(tc):
    len_arr = int(input())
    arr = list(map(int, input().split()))


    for i in range(len_arr - 1, 0, -1):                         # 버블 정렬
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    ans_list = []
    for i in range(5):
        ans_list.append(arr[len_arr - 1 - i])                   # 맨 오른쪽 값 (최대값) 부터 하나씩 내려옴
        ans_list.append(arr[i])                                 # 맨 왼쪽 값 부터 하나씩 올라감

    print(f'#{test_case+1}', end=' ')
    print(*ans_list)
