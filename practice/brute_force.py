def BruteForce(pattern, text):
    i = 0
    j = 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == len(pattern):
        return i - len(pattern)
    else:
        return 'fail'


print(BruteForce('tt','this is pattern'))