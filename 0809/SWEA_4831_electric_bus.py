# import sys
# sys.stdin = open('input.txt','r')

# 4831
tc = int(input())

def bus_charger(move, end, charger_num, charger):               # 문제 푸는 함수
    charging_count = 0
    start = 0
    for j in range(charger_num):                                # 이동거리 안에 충전기 없으면 0
        if charger[j+1] - charger[j] > move:
            return 0

    while start < end - move:                                   # 이동거리 안에 종점에 도착하는 상황이 아니라면 반복
        for k in range(start + move, start, -1):                # 이동거리 내에서 가장 먼 정류장부터 하나씩 역으로
            if k in charger:                                    # 만약 해당 정류장에 충전기가 있다면
                start = k                                       # 해당 정류장부터 다시 시작하는 걸로 하고
                charging_count += 1                             # 충전 횟수를 하나 올린 뒤,
                break                                           # for문을 나가서 wile문 반복으로 돌아감
    return charging_count


for i in range(tc):
    move, end, charger_num = tuple(map(int, input().split()))
    charger = [0] + list(map(int, input().split()))             # 시작점에 충전기 추가(j 범위 케어)
    print(f'#{i+1} {bus_charger(move,end,charger_num,charger)}')
