# 4834
tc = int(input())
for i in range(tc):
    num = int(input())
    arr =list(map(int, list(input())))
    count_arr = [0] * 10                # 카드 갯수를 세어둘 공간

    for j in arr:
        count_arr[j] += 1               # 카드 값에 해당하는 인덱스에 카운트
    max_num = 0
    max_idx = 0

    for j in range(10):
        if count_arr[j] >= max_num:
            max_num = count_arr[j]      # 가장 카운트가 많은 값을 찾고
            max_idx = j                 # 그 값의 인덱스가 그 카드에 적힌 수

    print(f'#{i + 1} {max_idx} {max_num}')
