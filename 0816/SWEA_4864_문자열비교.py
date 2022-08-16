tc = int(input())

for testcase in range(tc):
    pattern = input()
    target = input()
    ans = 0
    for i in range(len(target) - len(pattern) + 1):
        if target[i : i + len(pattern)] == pattern:
            ans = 1
            break
    
    print(f'#{testcase + 1} {ans}')
            