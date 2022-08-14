import sys
sys.stdin = open('input.txt','r')


def clockwise(N, arr):
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-1-i] = arr[i][j]
    return new_arr



tc = int(input())
for testcase in range(tc):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    arr90 = clockwise(N, arr)
    arr180 = clockwise(N, arr90)
    arr270 = clockwise(N, arr180)
    list90 = []
    list180 = []
    list270 = []

    
    
    for i in arr90:
        nums = ''.join(i)
        list90.append(nums)
    for i in arr180:
        nums = ''.join(i)
        list180.append(nums)
    for i in arr270:
        nums = ''.join(i)
        list270.append(nums)
    print(f'#{testcase+1}')
    for i in range(N):
        print(list90[i], list180[i], list270[i])
    
        
    