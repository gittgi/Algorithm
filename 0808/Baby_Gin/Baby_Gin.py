tc = int(input())

for i in range(tc):
    idx_list = [0] * 10
    triplet = 0
    run = 0
    num = list(map(int,list(input())))
    for j in num:
        idx_list[j] += 1 # 주어진 수를 인덱스로 하는 리스트에 개수만큼 더해주기
    j = 0
    while j < 10: # 인덱스(수) 9까지
        if idx_list[j] >= 3: # 세개보다 많이 있으면 
            triplet += 1  # triplet
            idx_list[j] -= 3 # triplet을 만드는데 사용된 수는 제거하고
            continue # 해당 수에서 또 triplet을 만들 수 있는지 확인
        else:
            j += 1 # 만들 수 없는 경우에는 다음 수 탐색
    j = 0 # 처음부터 다시 살펴보기 위해 초기화
    while j < 10: 
        if idx_list[j] >= 1 and idx_list[j+1] >= 1 and idx_list[j+2] >= 1: # 3연속으로 한 개 이상씩 있다면,
            run += 1 # run
            idx_list[j] -= 1 
            idx_list[j+1] -= 1
            idx_list[j+2] -= 1 # 사용된 수는 모두 제거
            continue # 같은 자리에서 또 run을 만들 수 있는지 검사
        else:
            j += 1 # 만들 수 없다면 다음 수 탐색
    if triplet + run == 2: # triplet 과 run 을 합쳐 2개가 된다면
        print(1) # 1을 출력
    else:
        print(0) # 아니라면 2를 출력