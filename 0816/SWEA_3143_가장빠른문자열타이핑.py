

tc = int(input())
for testcase in range(tc):
    target, pattern = tuple(input().split())
    original_len_target = len(target)
    cnt = 0
    while len(target) > 0:
        if target[:len(pattern)] == pattern:        
            cnt += 1
            target = target[len(pattern):]                  # 패턴을 찾으면 거기까지 자르고 다시 검사
        else:
            target = target[1:]                             # 못찾으면 한칸 자르고 검사
    
    print(cnt)
    ans = original_len_target - (len(pattern) * cnt) + cnt  


    
    


    print(f'#{testcase + 1} {ans}')


