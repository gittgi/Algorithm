
num = int(input())

for i in range(num):
    nums = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if nums[0] > nums[1]:     # 항상 b가 a 보다 길도록
        a, b = b, a
    
    cases = len(b) - len(a) + 1  # 조합 가능한 매치업의 수
    com_list = []
    for j in range(cases): 
        com = 0
        for k in range(len(a)):
            com += a[k] * b[k + j] # 첫 번째 조합은 a[0] * b[0] + ..., 그 다음 조합은 a[0] * b[0 + 1] + ...,
        com_list.append(com) # 그렇게 모은 조합의 곱합연산 결과 중 max
    print(f'#{i + 1} {max(com_list)}')    



