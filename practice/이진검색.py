def BinarySearch(arr, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if key == arr[middle]:
            return middle
        elif key > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return False


print(BinarySearch([1,2,3,4,5,6,7,8,9], 9, 11))