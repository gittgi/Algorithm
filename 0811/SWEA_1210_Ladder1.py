
import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if ladder[99][j] == 2:                                      # 도착지점을 찾아 역추적
            x, y = 99, j                                            # 현재 좌표는 x, y

    while x != 0:                                                   # x값이 맨위에 도착하면 끝남
        if 0 < y < 99:                                              # 맨 가장자리가 아니라면
            if ladder[x][y-1] == 1:                                 # 왼쪽이 1인경우,
                while ladder[x][y-1] != 0:                          # 왼쪽칸이 1이 아닐때 까지
                    y -= 1                                          # 계속해서 왼쪽으로 이동
                    if y == 0:                                      # 만약 이동했는데 가장자리가 되었다면
                        break                                       # 멈춘다.
                x -= 1                                              # 0을 만났거나 가장자리에 도달해서 멈췄다면 위로한칸 이동
            elif ladder[x][y+1] == 1:                               # 오른쪽도 왼쪽과 마찬가지로 작동
                while ladder[x][y+1] != 0:
                    y += 1
                    if y == 99:
                        break
                x -= 1
            else:
                x -= 1

        elif y == 0:                                                # 왼쪽 가장자리에서는 오른쪽으로 이동하는 것만 구현
            if ladder[x][y+1] == 1:
                while ladder[x][y+1] != 0:
                    y += 1
                    if y == 99:                                     # 혹시 만약에 쭉 이어져있는 경우 대비(시작지점이 0, 99밖에 없을때)
                        break
                x -= 1                                              # 이동이 막히면 위로 한칸
            else:
                x -= 1                                              # 오른쪽에 길이 없으면 위로 한칸

        else:                                                       # 오른쪽 가장자리도 마찬가지로 왼쪽으로 이동하는 것만 구현
            if ladder[x][y-1] == 1:
                while ladder[x][y-1] != 0:
                    y -= 1
                    if y == 0:
                        break
                x -= 1
            else:
                x -= 1
        # 매 단계마다 길이 있으면 그 방향으로 계속 이동하고, 길이 막히거나 끊기면 위로 한칸 이동 후 다시 좌우를 판단.
        # x가 0이 되면, 즉 목표에 도달하면 해당 y좌표 읽음

    print(f'#{tc} {y}')