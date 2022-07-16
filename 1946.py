T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    s_list = [input() for k in range(num)]

    ans = ''

    for i in range(num):
        ans += s_list[i][0] * int(s_list[i][2:])

    print(f'#{test_case}')
    for j in range(len(ans)):
        if (j + 1) % 10 == 0:
            print(ans[j] + '\n', end='')
        else:
            print(ans[j], end='')
    print('\n',end='')