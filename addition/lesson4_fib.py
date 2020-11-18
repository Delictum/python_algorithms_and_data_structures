import cProfile
import functools


def test_fib(func):
    sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(sequence):
        assert func(i) == item
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = 0, 1

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)


def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n+1):
        first, second = second, first + second

    return second


@functools.lru_cache()
def fib_cash(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


test_fib(fib_loop)

# test_fib(fib_dict)
# cProfile.run("fib_dict(20)")

# cProfile.run("fib_dict(10)")
# 23 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4_fib.py:11(fib_dict)
#      19/1    0.000    0.000    0.000    0.000 lesson4_fib.py:14(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("fib_dict(15)")
# 33 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4_fib.py:11(fib_dict)
#      29/1    0.000    0.000    0.000    0.000 lesson4_fib.py:14(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("fib_dict(20)")
# 43 function calls (5 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson4_fib.py:11(fib_dict)
#      39/1    0.000    0.000    0.000    0.000 lesson4_fib.py:14(_fib_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# f.fib_dict(10)
# 1000 loops, best of 5: 4.78 usec per loop

# f.fib_dict(15)
# 1000 loops, best of 5: 7.53 usec per loop

# f.fib_dict(20)
# 1000 loops, best of 5: 9.22 usec per loop

# test_fib(fib)

# cProfile.run('fib(10)')
# 180 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     177/1    0.000    0.000    0.000    0.000 lesson4_fib.py:11(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#    1973/1    0.001    0.000    0.001    0.001 lesson4_fib.py:11(fib)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.006 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#   21891/1    0.006    0.000    0.006    0.006 lesson4_fib.py:11(fib)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# "f.fib(10)"
# 1000 loops, best of 5: 29.3 usec per loop

# "f.fib(15)"
# 1000 loops, best of 5: 360 usec per loop

# "f.fib(20)"
# 1000 loops, best of 5: 3.96 msec per loop

#
