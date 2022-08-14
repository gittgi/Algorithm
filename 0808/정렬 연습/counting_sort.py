# 정렬하고자 하는 배열 : arr
# 숫자 갯수를 셀 배열 : arr_count
# 최종적으로 정렬 결과를 반환하는 배열 : arr_result

arr = [7,4,5,3,2,4,5,8,3,4]

max_arr = 0
for i in arr:  # 배열의 최대값 n을 구함
    if i > max_arr:
        max_arr = i

len_arr = 0 # len(arr) 대신
for i in arr:
    len_arr += 1



arr_count = [0] * (max_arr + 1)
arr_result = [0] * (len_arr)

for i in range(len_arr):
    arr_count[arr[i]] += 1 # arr의 값을 인덱스로 하는 arr_count 칸에 1씩 적립

for i in range(1, len(arr_count)):
    arr_count[i] += arr_count[i-1] # 누적 카운트를 센다

for i in range(len_arr-1,-1,-1): # arr의 뒤에서부터 센다.
    arr_count[arr[i]] -= 1 # 누적 카운트에서 하나를 빼고,
    arr_result[arr_count[arr[i]]] = arr[i] # 그 값을 인덱스로 해서 arr[i]를 넣는다.


print(arr_result)