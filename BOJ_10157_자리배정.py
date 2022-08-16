C, R = tuple(map(int, input().split()))
customer = int(input())

arr = [[0]*C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = R - 1, 0
num = 1
n = 0
if customer > C*R:
    print(0)

else:
    while num <= customer:
        
        if 0 <= x <= R - 1 and 0 <= y <= C - 1 and arr[x][y] == 0:
            arr[x][y] = num
            num += 1
            x += dx[n%4]
            y += dy[n%4]
        else:
            x -= dx[n%4]
            y -= dy[n%4]
            n += 1
            x += dx[n%4]
            y += dy[n%4]
    print((y - dy[n%4]) + 1, R - (x - dx[n%4]))
    


