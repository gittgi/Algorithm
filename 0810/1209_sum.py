
import sys
sys.stdin = open('input.txt', 'r')

tc = 10

for tc in range(tc):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = 0

    for i in range(100):                                           # 0 부터 99까지 행 하나를 고정
        total = 0                                                  # 행 별 합산을 초기화
        for j in range(100):                                       # i번 행 위의 모든 칸을 합산
            total += arr[i][j]
        if total > maxV:                                           # i행 합계가 지금까지의 최대값보다 크면 저장
            maxV = total                                           # 모든 i행에 대하여 반복

    for j in range(100):                                           # 고정하는 방향을 열로 바꾸고 j열 위의 모든 칸 합산
        total = 0
        for i in range(100):
            total += arr[i][j]
        if total > maxV:                                           # j열의 합계가 지금까지의 최대값보다 크면 저장
            maxV = total

    total = 0
    for i in range(100):
        total += arr[i][i]                                         # 행과 열의 인덱스 값이 같은, 즉 대각선을 합산
    if total > maxV:
        maxV = total

    total = 0
    for i in range(100):                                           # 행이 증가할 때 열이 감소하는 대각선을 합산
        total += arr[i][99-i]
    if total > maxV:
        maxV = total


    print(f'#{num} {maxV}')