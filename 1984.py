tc = int(input())

for i in range(tc):
    num_list = list(map(int, input().split()))
    new_list = sorted(num_list)[1:-1]
    print(f'#{i+1} {int(round(sum(new_list)/len(new_list),0))}')