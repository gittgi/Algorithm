import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())

for testcase in range(tc):
    arr = [list(input().split()) for _ in range(9)]

    ans = 1
    dx = [1, 1, 1, -1, -1, -1, 0, 0, 0]
    dy = [0, -1, 1, 0, -1, 1, 0, -1, 1]
    center = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]

    for a, b in center:
        sudoku = set()
        for i in range(9):
            x = a + dx[i]
            y = b + dy[i]
            sudoku.add(arr[x][y])
        if len(sudoku) != 9:
            ans *= 0
            break
    
    for i in range(9):
        sudoku_a = set()
        sudoku_b = set()
        for j in range(9):
            sudoku_a.add(arr[i][j])
            sudoku_b.add(arr[j][i])
        if len(sudoku_a) != 9 or len(sudoku_b) != 9:
            ans *= 0
            break

    print(f'#{testcase + 1} {ans}')