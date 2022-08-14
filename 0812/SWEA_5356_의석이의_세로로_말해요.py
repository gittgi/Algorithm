tc = int(input())

for testcase in range(tc):
    word_list = [input() for _ in range(5)]

    max_len = 0
    for i in word_list:
        if len(i) > max_len:
            max_len = len(i)
    
    for i in range(5):
        if len(word_list[i]) < max_len:
            word_list[i] += ' '*(max_len - len(word_list[i]))
    new_word = ''
    for j in range(max_len):
        for i in range(5):
            new_word += word_list[i][j]
    new_word_list = new_word.split()
    ans = ''.join(new_word_list)
    print(f'#{testcase + 1} {ans}')
