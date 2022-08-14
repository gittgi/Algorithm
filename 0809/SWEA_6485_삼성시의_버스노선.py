tc = int(input())

for num in range(tc):
    noseon = [0] * 5000                         # 5000개짜리 노선 준비
    N = int(input())
    for i in range(N):
        A, B = tuple(map(int, input().split()))
        for j in range(A - 1, B):               # A역부터 B역까지, 해당 버스가 지나갈 때 마다 역에 +1
            noseon[j] += 1
    ans_list = []                               # 결과 리스트
    p = int(input())
    for i in range(p):                          # 알고 싶은 역의 개수
        station = int(input())                  # 알고싶은 역의 번호
        ans_list.append(noseon[station - 1])    # 역의 번호대로, 버스가 지나갈때마다 1씩 더해줬던 값을 추출

    print(f'#{num + 1}', end=' ')
    print(*ans_list)