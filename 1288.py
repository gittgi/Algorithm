test_case = int(input())

for i in range(test_case):
    num = int(input())
    n = 0
    digit_set = set()
    while digit_set != {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        n += 1
        str_num = str(num * n)
        digit_set.update(list(str_num))
    print(f'#{i + 1} {num * n}')