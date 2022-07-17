a, b = map(int, input().split())



if (a - b) ** 2 == 1:
    if a > b:
        winner = 'A'
    else:
        winner = 'B'
else:
    if a == 3:
        winner = 'B'
    else:
        winner = 'A'

print(winner)
