tc = int(input())

for test_case in range(tc):
    N, K = tuple(map(int, input().split())) # N은 부분집합의 길이, K는 합
    arr = list(range(1,13))                 # 1부터 12까지의 리스트
    comb = []                               # 부분집합들을 보관할 리스트
    ans = 0                                 # 답 개수
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(arr[j])
        comb.append(temp)                   # 부분집합을 모두 구해서 리스트에 보관

    for i in comb:                          # 부분집합들 중에서 길이가 N이고 합이 K인 부분집합 찾기
        sub_len = 0
        sub_sum = 0
        for j in i:
            sub_len += 1
            sub_sum += j
        if sub_len == N and sub_sum == K:
            ans += 1                        # 찾으면 답 개수 증가

    print(f'#{test_case + 1} {ans}')
