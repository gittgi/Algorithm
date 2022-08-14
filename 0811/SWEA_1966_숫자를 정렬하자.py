
import sys
sys.stdin = open('input.txt','r')

tc = int(input())

for test_case in range(tc):
    length = int(input())
    arr = list(map(int, input().split()))

    for i in range(0,length-1):                                # 앞부분부터 정렬 된 곳은 건드리지 않기 위해 + 마지막은 굳이 안거드려도 되기에 범위 설정
        min_val = arr[-1]                                      # 일단 최소값은 대충 끝값(첫값은 진짜 최소값이 갈 자리라 안됨)
        min_val_idx = -1                                       # 일단 인덱스도 아무거나
        for j in range(i,length):                              # 맨뒤에까지 살펴보되 정렬 될때마다 앞부분은 한칸씩 정렬 된 상태이기에 잘라서 범위 설정
            if arr[j] < min_val:                               # 범위 내 최소값 찾기
                min_val = arr[j]
                min_val_idx = j                                # 최소값이 정해질 때마다 인덱스도 같이 기억해둠
        arr[i], arr[min_val_idx] = arr[min_val_idx], arr[i]    # 최종적으로 정해진 최소값의 인덱스로 해당 범위의 맨앞으로

    print(f'#{test_case+1}', end=' ')
    print(*arr)
