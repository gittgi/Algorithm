def combination(arr):
    n = len(arr)
    final = []
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp.append(arr[j])

        final.append(temp)
    return final


print(combination([1, 2, 3, 4]))
