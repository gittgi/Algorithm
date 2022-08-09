import sys
sys.stdin = open('input.txt','r')

tc = int(input())
for i in range(tc):
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    score_a = [0]*4
    score_b = [0]*4
    for j in list_a[1:]:
        score_a[j-1] += 1 # 인덱스 0부터 3까지 차례대로 세모, 네모, 동그라미, 별의 갯수가 담긴 리스트
    for j in list_b[1:]:
        score_b[j-1] += 1
    j = 3
    while j >= 0: # 스코어 리스트의 역순으로, 즉 별의 갯수부터 비교, 같으면 이전 인덱스 비교
        if score_a[j] > score_b[j]:
            print('A')
            break
        elif score_a[j] < score_b[j]:
            print('B')
            break
        else:
            j -= 1
    else: # 만약 인덱스 0까지 무승부라면 D출력
        print('D')
