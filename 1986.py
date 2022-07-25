num = int(input())

for i in range(num):
    zig_num = int(input())
    zig_sum = 0
    for j in range(1, zig_num + 1):
        if j % 2 == 1:
            zig_sum += j 
        elif j % 2 == 0:
            zig_sum -= j
    print(f'#{i+1} {zig_sum}')
