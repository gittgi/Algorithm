def select(arr, k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr[k-1]


print(select([1,4,3,6,7,8,0], 2))