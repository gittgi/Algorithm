n = int(input())

numbers = list(map(int, input().split()))

numbers.sort()

mid = numbers[n // 2]





print(mid)