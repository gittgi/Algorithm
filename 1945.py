case = int(input())

for i in range(case):
    num = int(input())
    divide_list = [2,3,5,7,11]
    count_list = []
    for j in divide_list:
        count = 0
        while num % j == 0:
            num /= j
            count += 1
        count_list.append(count)

    print(f'#{i+1}',end=' ')
    print(*count_list)

