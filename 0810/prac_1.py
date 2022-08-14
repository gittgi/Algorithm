import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())

for test_case in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):
            if i - 1 >= 0:                                      # 위칸이 맨위 경계(0)를 벗어나면 이웃하는 칸이 없음
                dif = arr[i][j] - arr[i-1][j]                   # 기준 좌표 위에 있는 칸과의 비교
                if dif > 0:                                     # 차이가 양수 일 때와 음수일 때 나눠서 합산 (abs 대용)
                    total += dif
                else:
                    total += dif * (-1)

            if i + 1 < n:                                       # 아래칸이 최대칸(n-1)을 벗어나면 안됨
                dif = arr[i][j] - arr[i + 1][j]                 # 아래칸 과의 비교 및 양수 음수 나눠서 합산
                if dif > 0:
                    total += dif
                else:
                    total += (dif * (-1))

            if j - 1 >= 0:                                      # 좌우로도 같은 처리를 반복
                dif = arr[i][j] - arr[i][j - 1]
                if dif > 0:
                    total += dif
                else:
                    total += (dif * (-1))

            if j + 1 < n:
                dif = arr[i][j] - arr[i][j + 1]
                if dif > 0:
                    total += dif
                else:
                    total += (dif * (-1))

    print(total)




