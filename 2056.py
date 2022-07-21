num = int(input())

for i in range(num):
    ymd = input() # 문자열로 받아서
    y = ymd[:4] 
    m = ymd[4:6]
    d = ymd[6:]
    if int(m) > 12 or int(m) < 1: # 월 범위 체크
        ans = -1
    else:
        if int(m) in [1, 3, 5, 7, 8, 10, 12]: # 31일까지 있는 달
            if int(d) > 31 or int(d) < 1:
                ans = -1
            else: 
                ans = y + '/' + m + '/' + d
        elif int(m) in [4, 6, 9, 11]: # 30일까지 있는 달
            if int(d) > 30 or int(d) < 1:
                ans = -1
            else:
                ans = y + '/' + m + '/' + d
        else: # 28일까지 있는 달 (2월)
            if int(d) > 28 or int(d) < 1:
                ans = -1
            else:
                ans = y + '/' + m + '/' + d
    
    print(f'#{i + 1} {ans}')