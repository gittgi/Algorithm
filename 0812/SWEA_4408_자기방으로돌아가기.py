tc = int(input())

for a in range(tc):
    hotel = [set() for _ in range(200)]
    num = int(input())
    for b in range(num):
        room = list(map(int,input().split()))
        s = room[0]
        e = room[1]
        if e < s:
            s,e = e,s
        for i in range(s-1,e):
            hotel[i//2].add(b)

        max_len = 0
        for i in hotel:
            if len(i) > max_len:
                max_len = len(i)
    print(f'#{a + 1} {max_len}')
