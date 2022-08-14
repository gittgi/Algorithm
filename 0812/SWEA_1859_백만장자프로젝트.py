tc = int(input())

# 기본적으로 최대값일 때까지 계속 구매하다가, 최대값인 날에 팔고, 다시 남은 날 중의 최대값까지 기다리는 것을 반복합니다.

for i in range(tc):
    
    margin = 0
    num = int(input())
    num_list = list(map(int,input().split()))
    while len(num_list) > 0:
        selling_day = num_list.index(max(num_list)) # 최대값인 날 확인
        # (최대값 * 지금까지 산 개수) - 최대값인 날 직전까지 구입하는데 쓴 돈
        margin += num_list[selling_day]*len(num_list[:selling_day]) - sum(num_list[:selling_day]) 
    
        num_list = num_list[selling_day+1:] # 지나간 날은 지우고 다시 반복
    print(f'#{i+1} {margin}')