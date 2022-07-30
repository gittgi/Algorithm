tc = int(input())
 
for i in range(tc):
    games = input()
    left_games = 15 - len(games)
    if games.count('o') + left_games >= 8:
        print(f'#{i + 1} YES')
    else:
        print(f'#{i + 1} NO')