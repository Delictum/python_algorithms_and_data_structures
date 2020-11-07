def primes():
    num = 2
    while True:
        is_simple = True
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


for _ in range(30):
    for i in primes():
        print(i)
