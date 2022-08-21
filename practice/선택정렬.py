def selectionsort(arr, N):
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if arr[j] < arr[minidx]:
                minidx = j

        arr[i], arr[minidx] = arr[minidx], arr[i]
    return  arr


print(selectionsort([6, 4, 5, 2, 45, 3, 6, 7, 2, 6, 8], 11))