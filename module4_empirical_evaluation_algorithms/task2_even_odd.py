"""
The task 2:
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import cProfile


def get_even_odd(num):
    count_odd = 0
    count_even = 0

    for i in num:
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


# cProfile.run("get_even_odd('1234567890')")
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2_even_odd.py:10(get_even_odd)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run("get_even_odd('12345678906321647698472627344876138476781768934764532153215236346432636462621346191')")
# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2_even_odd.py:10(get_even_odd)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.task2_even_odd as t" "t.get_even_odd('1234567890')"
# 1000 loops, best of 5: 2.97 usec per loop

# python -m timeit -n 1000 -s "import module4_empirical_evaluation_algorithms.task2_even_odd as t" "t.get_even_odd('12345678906321647698472627344876138476781768934764532153215236346432636462621346191')"
# 1000 loops, best of 5: 26.4 usec per loop
