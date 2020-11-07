s = input()
a = input()
b = input()

i = 0
while a in s:
    i += 1
    s = s.replace(a, b)
    if i > 1000:
        print('Impossible')
        break
else:
    print(i)
