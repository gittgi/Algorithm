n = int(input())

word = set()


for i in range(n):
    word.add(input())

word = list(word)

for i in range(len(word), -1, -1):
    for j in range(i-1):
        if len(word[j]) > len(word[j+1]):
            word[j], word[j+1] = word[j+1], word[j]
        elif len(word[j]) == len(word[j+1]):
            if word[j] > word[j+1]:
                word[j], word[j+1] = word[j+1], word[j]
for i in range(len(word)):
    print(word[i])

