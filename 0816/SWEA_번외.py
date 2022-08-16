import sys
sys.stdin = open('input.txt', 'r')


def palindrome(arr):

    for M in range(len(arr),0,-1):
        for i in range(len(arr)):
            for j in range(len(arr) - M + 1):
                row = arr[i][j:j+M]
                if row == row[::-1]:
                    return M
tc = 10
for testcase in range(tc):
    test_num = int(input())
    arr = list(input())
    
    ans1 = palindrome(arr)
    

    
    print(f'#{testcase + 1} {ans1}')