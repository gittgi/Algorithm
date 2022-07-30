test_case = int(input())
for i in range(test_case):
    n = int(input())
    
    player = list(map(int, input().split()))
    count = 0
    player.sort(reverse=True)
    while player[1] > 0:
        player[0] -= 1
        player[1] -= 1
        count += 1
        player.sort(reverse=True)

    print(f'#{i + 1} {count}')