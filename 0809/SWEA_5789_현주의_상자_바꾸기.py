tc = int(input())

for i in range(tc):
    N, Q = tuple(map(int, input().split()))
    arr = [0] * N                                   # N개의 상자 초기값
    for j in range(Q):
        L, R = tuple(map(int, input().split()))
        for k in range(L-1, R):                     # L번 상자부터 R번 상자까지
            arr[k] = j + 1                          # j+1번째(j는 0부터 시작) 작업이니까 j+1로 상자 값 변경
    print(f'#{i + 1}', end=' ')
    print(*arr)