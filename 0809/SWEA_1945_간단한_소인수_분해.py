case = int(input())

for i in range(case):
    num = int(input())
    divide_list = [2, 3, 5, 7, 11]  # 인수분해할 리스트
    count_list = []                 # 인수분해할 숫자별로 몇승인지 카운트를 담아둘 리스트

    for j in divide_list:           # 2, 3, 5, 7, 11 순으로
        counter = 0
        while num % j == 0:         # 계속해서 나누어 떨어지는 동안에는
            num /= j                # 일단 원래 숫자를 나누고
            counter += 1            # 나눴으니까 1승을 올려줌
        count_list.append(counter)  # 나누어 떨어지지 않으면 지금까지 나눈 횟수만큼 리스트에 추가
                                    # 어차피 순서대로 나누고, 그 순서대로 출력해야 하기 때문에 append로 순서대로 저장

    print(f'#{i + 1}', end=' ')
    print(*count_list)