# x축의 길이
# 쌓여있는 상자의 높이 나열

import sys

sys.stdin = open('input.txt','r')

tc = int(input())
for n in range(tc):
    num = int(input())
    arr = list(map(int,input().split()))

    max_gap = 0
    for i in range(num):            # i는 기준이 되는 열
        gap = 0
        for j in range(i+1,num):    # 기준 열 보다 왼쪽에 있는 열들과 일일이 비교
            if arr[i] > arr[j]:     # 기준 열이 왼쪽에 있는 열보다 큰 경우
                gap += 1            # 낙차도 한칸 늘어난다.
        if gap > max_gap:           # 기준열을 마지막 열까지 비교해서 모은 낙차가 현재까지 최고 낙차라면,
            max_gap = gap           # 그 값을 최고 낙차로 재할당하고 다시 다음열을 기준열로 삼아서 비교 반복

    print(f'#{n+1} {max_gap}')

