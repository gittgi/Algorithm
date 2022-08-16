import sys
sys.stdin = open('input2.txt', 'r')


def palindrome(arr):

    for M in range(100,0,-1):
        for i in range(100):
            for j in range(100 - M + 1):
                row = arr[i][j:j+M]
                if row == row[::-1]:
                    return M
tc = 10
for testcase in range(tc):
    test_num = int(input())
    arr = [list(input()) for _ in range(100)]
    
    ans1 = palindrome(arr)
    new_arr = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            new_arr[j][i] = arr[i][j]
    ans2 = palindrome(new_arr)
    if ans1 > ans2:
        ans = ans1
    else:
        ans = ans2

    
    print(f'#{testcase + 1} {ans}')