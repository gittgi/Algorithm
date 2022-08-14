# 4835
tc = int(input())

for i in range(tc):
    length, interval = tuple(map(int, input().split()))
    num_list = list(map(int, input().split()))
    count_list = [0] * (length - interval + 1)          # 구간별로 합계를 저장할 리스트
    for j in range(length-interval + 1):                # 처음부터 마지막 조합까지
        sum_num = 0
        for k in num_list[j:j+interval]:                # 그 구간의 원소들을 다 더해서
            sum_num += k
        count_list[j] = sum_num                         # 리스트에 저장해둔다
    max_num = 0
    min_num = count_list[0]
    for j in count_list:                                # 구간별로 합계를 다 모아둔 리스트의 최대값, 최소값 찾기
        if j > max_num:
            max_num = j
        if j < min_num:
            min_num = j
    print(f'#{i + 1} {max_num - min_num}')