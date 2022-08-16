import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())

for testcase in range(tc):
    N, M = tuple(map(int,input().split()))
    arr = [list(input()) for _ in range(N)]
       
    for i in range(N):              
        for j in range(N - M + 1):         
            row = arr[i][j:j+M]
            if row == row[::-1]:
                ans = (''.join(row))         
            
    new_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][i] = arr[i][j]
        
        
    for i in range(N):
        for j in range(N - M + 1):
            row = new_arr[i][j:j+M]
            if row == row[::-1]:
                ans = (''.join(row))
        

        
        
    print(f'#{testcase + 1} {ans}')