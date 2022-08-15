num = int(input())
board = [['0']*1001 for _ in range(1001)]
name_list = []
for i in range(num):
    name_list.append(f'{i+1}')
for s in range(num):
    paper = list(map(int,input().split()))
    for i in range(paper[1],paper[3]+paper[1]):
        for j in range(paper[0],paper[2]+paper[0]):
            board[i][j] = name_list[s]



for s in range(num):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if board[i][j] == f'{s+1}':
                cnt += 1
    print(cnt)