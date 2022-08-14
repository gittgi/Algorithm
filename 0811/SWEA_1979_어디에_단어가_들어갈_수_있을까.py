import sys
sys.stdin = open('input.txt','r')

tc = int(input())

for test_case in range(tc):
    N, K = tuple(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        space = 0
        for j in range(N):
            if arr[i][j] == 1:              # 행 고정 후 한칸 씩 1인지 확인
                space += 1                  # 1이라면 지금까지 연결되어 있는 1의 개수 기록
            else:                           # 만약 1이 끊겼다면,
                if space == K:              # 지금까지 이어진 1의 개수가 K인지 확인
                    ans += 1                # K개라면 정답 카운트 1개 추가
                    space = 0               # 다시 1을 새로 셀 수 있게 초기화
                else:
                    space = 0               # K개가 아니라면 다시 셀 수 있게 초기화
        if space == K:                      # 마지막 칸에 도착했을 때, 마지막 칸이 1이라면, 지금까지 K개를 세어도 정답에 기록 할 수 없음
            ans += 1                        # 따라서 다음 행으로 넘어가기 전에 한번 더 체크

    for j in range(N):                      # 이번엔 반대로 열을 고정시켜서 똑같이 반복
        space = 0
        for i in range(N):
            if arr[i][j] == 1:
                space += 1
            else:
                if space == K:
                    ans += 1
                    space = 0
                else:
                    space = 0
        if space == K:
            ans += 1

    print(f'#{test_case + 1} {ans}')

