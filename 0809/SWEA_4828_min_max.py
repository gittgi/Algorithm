import sys
sys.stdin = open('input.txt','r')

# 1208
tc = 10

def bubble(lst, n): # 버블소트
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

for i in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    arr_len = 0
    for j in arr:                                   # 소트를 위해 리스트의 길이 구하기 (len 대용)
        arr_len += 1
    arr = bubble(arr, arr_len)                      # 주어진 상자더미를 높이 순서로 오름차순 정렬
    for j in range(dump):                           # 정해진 횟수만큼 가장 높은곳에서는 빼고, 가장 낮은 곳에서는 더한다.
        arr[0] += 1
        arr[-1] -= 1
        arr = bubble(arr, arr_len)                  # 다시 정렬해서 높이가 역전되지 않도록 맞추고 반복

    print(f'#{i + 1} {arr[-1] - arr[0]}')
