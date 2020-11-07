n = int(input())

if n < 3:
    print(1, '\n', n, sep='')
else:
    i = 0
    mas = []
    
    while 1:
        i += 1
        if (i*2 < n):
            mas.append(i)
            n -= i
        else:
            mas.append(n)
            break

    print(len(mas))
    for elem in mas:
        print(elem, end=' ')
