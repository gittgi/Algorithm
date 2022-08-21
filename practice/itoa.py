def itoa(n):
    temp = []
    while n != 0:
        temp.append(n % 10)
        n //= 10
    ans = ''
    for i in temp[::-1]:
        ans += chr(i+48)

    return ans

print(type(itoa(123)))