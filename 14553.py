test_case = int(input())


for i in range(test_case):
    n = int(input())
    
    player = list(map(int, input().split()))
    
    count = sum(player) // 2   

    print(f'#{i + 1} {count}')

'''
여기는 어렵게 푼 버전 (메모리 초과 됨)
for i in range(test_case):
    n = int(input())
    
    player = list(map(int, input().split()))
    count = 0
    while sum(player) > 1:
        player.sort(reverse=True)
        count += player[1]
        player[0] -= player[1]
        player.pop(1) 

    print(f'#{i + 1} {count}')
'''