import sys
sys.stdin = open('input.txt','r')



def bug_kill(start_x ,start_y ,M):                  # x,y칸을 시작으로 하는 M크기의 상자들의 합
    total = 0
    for i in range(M):
        for j in range(M):
            total += arr[start_x + i][start_y + j]
    return total

tc = int(input())

for testcase in range(tc):
    N, M = tuple(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0
    for i in range(N-M+1):                                      # M크기의 상자가 범위를 넘어가지 않도록 범위 조정
        for j in range(N-M+1):
            if bug_kill(i,j,M) > max_total:
                max_total = bug_kill(i,j,M)

    print(f'#{testcase + 1} {max_total}')
