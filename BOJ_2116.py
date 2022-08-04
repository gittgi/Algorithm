# 첫번째에 어떤 눈을 선택해서 쌓기 시작하느냐에 따라 결과가 정해짐
# 따라서 6가지 경우의 수만 구하면 답

import copy # 딥카피용

tc = int(input()) 
dict = {0:5,1:3,2:4,3:1,4:2,5:0} # 주사위 맞은편 인덱스 찾기용 사전
dices = [] 
for h in range(tc):
    dices.append(list(map(int,input().split()))) # 주사위 저장
dices_to_refill = copy.deepcopy(dices) # 주사위 복사본
sum_list = [] 
for i in range(6): # 첫번째 주사위의 모든 눈에 대해서
    num_to_add = 0
    dices = copy.deepcopy(dices_to_refill) # 주사위 원본 복원
    chosen = dices[0][i] # 첫 주사위의 한 눈 선택
    opposite = dices[0][dict[i]] # 반대면
    dices[0].remove(chosen) # 선택한 눈과
    dices[0].remove(opposite) # 반대 눈을 제거
    num_to_add += max(dices[0]) # 남은 눈 (옆면들) 중에 가장 큰 수 더함
    for j in range(1,len(dices)): # 남은 주사위들로 반복
        if num_to_add < 7: # 만약 아직 반복을 한번도 하지 않았다면 (그래서 옆면의 합이 아직 7보다 작다면)
            new_chosen = opposite # 첫 주사위의 반대면을 새 선택 눈으로 사용
        else: # 만약 반복을 한번 이상 했다면
            new_chosen = new_opposite # 반복문 끝의 변수(맞은편 눈)를 새 선택 눈으로 가져옴
        new_opposite = dices[j][dict[dices[j].index(new_chosen)]] # j+1번째 주사위의 맞은편 눈 구하기
        dices[j].remove(new_chosen) 
        dices[j].remove(new_opposite) # 선택된 눈과 맞은편 눈 제거
        num_to_add += max(dices[j]) # 남은 눈 중 최대값 더하기
    sum_list.append(num_to_add) # 첫번째 주사위의 각 눈부터 시작하는 6개의 루트를 따라가며 모은 최대값들의 합
print(max(sum_list)) # 그 중의 최대값



        






