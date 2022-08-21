def atoi(s):
    num = 0
    for i in range(len(s)):
        num += (10 ** (len(s) - i - 1)) * (ord(s[i]) - 48)

    return(num)


print(type(atoi('123')))
