tc = int(input())

for test_case in range(tc):
    arr = list(map(int, input().split()))
    combination = []                        # 부분집합들을 담을 리스트
    for i in range(1, 1 << 10):             # 0일때는 공집합이 나오므로 제외하고 가능한 조합 만큼 반복
        temp = []                           # 한가지의 조합을 임시로 보관할 리스트
        for j in range(10):
            if i & (1 << j):
                temp.append(arr[j])         # j 한 사이클이 돌아갈 때 자리 마다 유무를 검사하고, 만약 있으면 임시로 리스트로 보관
        combination.append(temp)            # 임시로 보관해 둔 조합을 리스트의 형태 그대로 기록

    for i in combination:                   # 가능한 모든 조합(공집합 제외) 리스트들을 하나씩 검사
        total = 0
        for j in i:                         # 해당 조합을 하나하나 더해줌 (sum대용)
            total += j
        if total == 0:                      # 합이 0이라면 더 알아보지 않고 1 출력 후 종료
            print(1)
            break
    else:                                   # 합이 0이 되는 조합이 없어 break 하지 못한 경우 0을 출력
        print(0)



