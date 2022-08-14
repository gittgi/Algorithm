tc = int(input())

for test_case in range(tc):
    num = int(input())
    board = [[0] * 10 for _ in range(10)]               # 빈 보드
    for i in range(num):
        rect = list(map(int, input().split()))
        if rect[-1] == 1:                               # 빨강 네모
            for j in range(rect[0], rect[2]+1):         # 가로 좌표
                for k in range(rect[1], rect[3]+1):     # 세로 좌표
                    board[j][k] += 1                    # 1로 색칠
        else:                                           # 파랑 네모
            for j in range(rect[0], rect[2]+1):         # 가로 좌표
                for k in range(rect[1], rect[3]+1):     # 세로 좌표
                    board[j][k] += 2                    # 2로 색칠
    ans = 0
    for i in board:
        for j in i:
            if j == 3:                                  # 빨강과 파랑 합쳐져 있으면
                ans += 1                                # 칸수 하나 센다.

    print(f'#{test_case + 1} {ans}')


