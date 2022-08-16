w, h = tuple(map(int, input().split()))

x, y = tuple(map(int, input().split()))

t = int(input())

if ((t-(w-x))//w) % 2 == 1:
    x = (t-(w-x)) % w
else:
    x = w - ((t-(w-x)) % w)


if ((t-(h-y))//h) % 2 == 1:
    y = (t-(h-y)) % h
else:
    y = h - ((t-(h-y)) % h)
    
print(x, y)