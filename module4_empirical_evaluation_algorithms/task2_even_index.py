"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
"""

import random
import cProfile


def get_even_index(array):
    result = [i for i, e in enumerate(array) if e % 2 == 0]
    return result


# cProfile.run('get_even_index([random.randint(0, 9) for _ in range(10)])')
# 59 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:12(get_even_index)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:13(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('get_even_index([random.randint(0, 99) for _ in range(100)])')
#  531 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:12(get_even_index)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:13(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       125    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('get_even_index([random.randint(-999, 999) for _ in range(1000)])')
# 5035 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.004    0.004 <string>:1(<listcomp>)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1000    0.002    0.000    0.003    0.000 random.py:174(randrange)
#      1000    0.001    0.000    0.004    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:12(get_even_index)
#         1    0.000    0.000    0.000    0.000 task2_even_index.py:13(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1029    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task2_even_index as t" "t.get_even_index([random.randint(0, 9) for _ in range(10)])"
# 1000 loops, best of 5: 19.4 usec per loop

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task2_even_index as t" "t.get_even_index([random.randint(0, 99) for _ in range(100)])"
# 1000 loops, best of 5: 171 usec per loop

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task2_even_index as t" "t.get_even_index([random.randint(-999, 999) for _ in range(1000)])"
# 1000 loops, best of 5: 1.86 msec per loop