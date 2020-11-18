import cProfile
import functools


def get_simple_in_eratosthenes(n):
    """
    Нахождения i-го по счёту простого числа с решетом - а не формирование решето до заданного числа
    Алгоритм не идеален, слишком большой список создается изначально
    """
    if n == 0:
        return 2

    sieve = list(range((n + 1)**2))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0

        if i > n:
            result = [i for i in sieve if i != 0]
            if len(result) == n:
                break

    return result[n]


def get_simple_number(n):
    results = [2]
    base = 0
    i = results[0]
    while base < n:
        while True:
            i += 1
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                results.append(i)
                break

        base += 1

    return results[-1]


""" FUNCTION 1 - 'GET_SIMPLE_IN_ERATOSTHENES' """
# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_in_eratosthenes(1)"
# 1000 loops, best of 5: 3.96 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_in_eratosthenes(10)"
# 1000 loops, best of 5: 174 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_in_eratosthenes(20)"
# 1000 loops, best of 5: 1.57 msec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_in_eratosthenes(100)"
# Не дождался за 15 минут

# cProfile.run("get_simple_in_eratosthenes(1)")

# 10 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 simple_numbers.py:20(<listcomp>)
#         1    0.000    0.000    0.000    0.000 simple_numbers.py:5(get_simple_in_eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_in_eratosthenes(10)")

# 86 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        26    0.000    0.000    0.000    0.000 simple_numbers.py:20(<listcomp>)
#         1    0.000    0.000    0.000    0.000 simple_numbers.py:5(get_simple_in_eratosthenes)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        56    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_in_eratosthenes(20)")

# 243 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#        77    0.002    0.000    0.002    0.000 simple_numbers.py:20(<listcomp>)
#         1    0.000    0.000    0.002    0.002 simple_numbers.py:5(get_simple_in_eratosthenes)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       162    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_in_eratosthenes(100)")
# 3710 function calls in 0.579 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.579    0.579 <string>:1(<module>)
#      1227    0.566    0.000    0.566    0.000 simple_numbers.py:20(<listcomp>)
#         1    0.012    0.012    0.579    0.579 simple_numbers.py:5(get_simple_in_eratosthenes)
#         1    0.000    0.000    0.579    0.579 {built-in method builtins.exec}
#      2479    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

""" FUNCTION 2 - 'GET_SIMPLE_NUMBER' """

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_number(1)"
# 1000 loops, best of 5: 1.49 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_number(10)"
# 1000 loops, best of 5: 21.6 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_number(20)"
# 1000 loops, best of 5: 76.6 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.simple_numbers as t" "t.get_simple_number(100)"
# 1000 loops, best of 5: 1.98 msec per loop

# cProfile.run("get_simple_number(1)")

# 5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 simple_numbers.py:27(get_simple_number)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_number(10)")

# 14 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 simple_numbers.py:27(get_simple_number)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_number(20)")

# 24 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 simple_numbers.py:27(get_simple_number)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_simple_number(100)")
# 104 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 simple_numbers.py:27(get_simple_number)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
