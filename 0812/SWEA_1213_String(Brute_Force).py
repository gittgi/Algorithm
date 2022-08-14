# 패턴 찾고 카운트 올리고, 패턴 찾은 곳 다음부터 재귀로 반복해서 패턴 찾는 함수
def brute_force_rec(pattern, target, cnt):
    N = len(target)
    M = len(pattern)

    i = 0
    j = 0

    while i < N and j < M:
        if target[i] != pattern[j]:
            i = i - j
            j = -1

        i += 1
        j += 1

    if j == M:
        cnt += 1
        return brute_force_rec(pattern, target[i - M + 1:], cnt)    # 찾은 뒤엔 타겟 문장을 자르고, 카운트를 저장해서 다시 돌림 
    else:
        return cnt                                                  # 못찾으면 지금까지 센 카운트 반환





for test_case in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    ans = brute_force_rec(pattern, target, 0)                   # 카운트의 시작값은 당연히 0

    print(f'#{tc} {ans}')