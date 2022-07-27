case = int(input())

for i in range(case):
    num = int(input())
    divide_list = [2,3,5,7,11] # 인수분해 인수 목록
    count_list = []            # 각 수마다 인수분해 한 횟수 담는 리스트
    for j in divide_list:      # 2부터 차례대로
        count = 0
        while num % j == 0:    # 나눴을때 나누어 떨어지는 상황이라면,
            count += 1         # 카운트를 올리고
            num /= j           # 나눈 후의 값으로 다시 반복 -> 나누어 떨어지지 않을때까지
            count_list.append(count) # 리스트에 순서대로 담기

    print(f'#{i+1}',end=' ')
    print(*count_list)         # 이거 너무 좋아요!