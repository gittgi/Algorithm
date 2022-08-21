def pre_process(pattern):
    lps = [0] * len(pattern)

    j = 0

    for i in range(1, len(pattern)):
        if pattern[j] == pattern[i]:
            lps[i] = j + 1
            j += 1
        else:
            j = 0
            if pattern[j] == pattern[i]:
                lps[i] = j + 1
                j += 1

    return lps




def kmp(text, pattern):
    lps = pre_process(pattern)
    i = 0
    j = 0
    position = -1
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]

            else:
                i += 1

        if j == len(pattern):
            position = i - j
            break
    return position

print(kmp('gittgitgigittgitgi', 'itg'))