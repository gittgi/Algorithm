tc = int(input())
 
for i in range(tc):
    word = input()
    left_set = set()
    for j in word:
        if word.count(j) % 2 != 0:
            left_set.add(j)
    left_list = list(left_set)
     
    if left_list == []:
        print(f'#{i + 1} Good')
    else:
        left_string = ''.join(sorted(left_list))
        print(f'#{i + 1} {left_string}' )