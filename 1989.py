
num = int(input())
s_list = [input() for k in range(num)]

for i in range(num):
    ans = 1
    word = s_list[i].rstrip()
    for j in range(len(word) // 2):
        if word[j] == word[len(word) - j - 1]:
            ans *= 1
        else:
            ans *= 0

    print(f'#{i + 1} {ans}')