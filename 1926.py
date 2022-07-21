num = input()

for i in range(1, int(num) + 1): # 1부터 주어진 숫자까지
    num_369 = str(i).count('3') + str(i).count('6') + str(i).count('9') 숫자에 등장하는 3,6,9 개수
    if num_369 > 0: # 369가 있으면
        print('-' * (num_369) ,end=' ') # 그 개수만큼 - 출력
    else:
        print(i, end=' ') # 없으면 그냥 숫자 출력