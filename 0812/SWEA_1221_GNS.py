import sys
sys.stdin = open('input.txt', 'r')


alien_lang = dict(ZRO=0, ONE=1, TWO=2, THR=3, FOR=4, FIV=5, SIX=6, SVN=7, EGT=8, NIN=9) # 사전으로 번역

tc = int(input())
for test_case in range(tc):
    no = input().split()
    qnum = no[0]
    length = int(no[1])
    word_list = input().split()
    for k in range(length-1,-1,-1): # 버블 소팅
        for i in range(k):
            if alien_lang[word_list[i]] > alien_lang[word_list[i+1]]: # 딕셔너리로 값을 비교하고 정렬
                word_list[i], word_list[i+1] = word_list[i+1], word_list[i]

    print(f'{qnum}')
    print(*word_list)