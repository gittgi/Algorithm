import sys
sys.stdin = open('input.txt','r')

for i in range(10):
    ans = 0
    num = int(input())
    arr = list(map(int, input().split()))
    for j in range(2, num - 2): # 건물이 있는 곳만 계산
        max_nei = 0 # 이웃 두칸 건물들 중의 최대 높이
        for k in [j-2, j-1, j+1, j+2]: # 양 옆 두줄의 건물 중 최대 높이 구하기
            if arr[k] > max_nei: 
                max_nei = arr[k]
        if arr[j] - max_nei > 0: # 이웃 건물 중 최대 높이보다 내가 크다면,
            ans += (arr[j] - max_nei) # 그 큰 수치만큼이 내 건물에서 조망권이 확보되는 층 수
    print(f'#{i+1} {ans}')