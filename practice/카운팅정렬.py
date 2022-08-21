def counting(arr, N):
    ordered = [0]*N
    idx = [0]*(N+1)

    for i in range(N):
        idx[arr[i]] += 1

    for i in range(1, len(idx)):
        idx[i] += idx[i-1]

    for i in range(N-1,-1,-1):
        idx[arr[i]] -= 1
        ordered[idx[arr[i]]] = arr[i]

    return ordered

print(counting([8,4,3,5,6,9,9,2,1], 9))