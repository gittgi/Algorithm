n = int(input())
alist = []
for i in range(n):
    alist.append(list('0'*n))

for i in range(0, n - 1):
    alist[0][i] = i + 1

for i in range(n - 1):
    alist[i][n-1] = i + n
   
for i in range(n - 1):
    alist[n-1][n -1 -i] =  (2*n) - 1 + i

for i in range(n - 1):
    alist[n-1-i][0] = (3*n) - 2 + i


# 재귀함수로 접근해보기
# 그 다음은 1,1 부터 n-2, n-2
# 다음거 시작값은 어떻게 하지..






print(alist)