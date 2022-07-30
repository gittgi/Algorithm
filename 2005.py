

def pascal(n):
    new_list = list(map(int, '1'*n)) # ['1','1','1','1','1','1'...]
    if n == 1:
        return new_list
    else:
        for i in range(1, len(new_list)-1):
            new_list[i] = pascal(n-1)[i-1] + pascal(n-1)[i]
        return new_list

tc = int(input())

for i in range(tc):
    num = int(input())
    print(f'#{i+1}')
    for j in range(1, num+1):
        print(*pascal(j))