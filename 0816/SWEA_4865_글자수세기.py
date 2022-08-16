tc = int(input())

for testcase in range(tc):
    str1 = set(input())
    str2 = list(input())
    max_cnt = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    
    print(f'#{testcase + 1} {max_cnt}')