tc = int(input())

for testcase in range(tc):

    bar = input()

    laser_pointer = []
    for i in range(len(bar)-2):
        if bar[i:i+2] == '()':
            laser_pointer.append(i) # 레이저의 위치 찾기



    bar_list = list(bar)
    for i in laser_pointer:
        bar_list[i]= 'L'
        bar_list[i+1] = 'aser'      # 레이저의 위치 표시, aser는 그냥 자리차지용


    stick = 0
    piece = 0
    for i in bar_list:          
        if i == '(':                # 막대가 생김
            stick += 1
        elif i == 'L':              # 조각이 막대만큼 생김
            piece += stick
        elif i == ')':              # 막대가 하나 사라지고 조각이 하나 생김
            stick -= 1
            piece += 1
                                    
    print(f'#{testcase + 1} {piece}')