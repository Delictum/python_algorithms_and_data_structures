"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""


import random
import cProfile


def get_two_min(mas):
    return sorted(mas)[0:2]


# cProfile.run("get_two_min([random.randint(0, 9) for i in range(10)])")
# 60 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task7_two_min.py:11(get_two_min)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run("get_two_min([random.randint(0, 99) for i in range(100)])")
# 534 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task7_two_min.py:11(get_two_min)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run("get_two_min([random.randint(0, 999) for i in range(1000)])")
# 5042 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.004    0.004 <string>:1(<listcomp>)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1000    0.001    0.000    0.003    0.000 random.py:174(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task7_two_min.py:11(get_two_min)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1036    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task7_two_min as t" "t.get_two_min([random.randint(0, 9) for _ in range(10)])"
# 1000 loops, best of 5: 17 usec per loop

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task7_two_min as t" "t.get_two_min([random.randint(0, 99) for _ in range(100)])"
# 1000 loops, best of 5: 163 usec per loop

# python -m timeit -n 1000 -s "import random;import module4_empirical_evaluation_algorithms.task7_two_min as t" "t.get_two_min([random.randint(0, 999) for _ in range(1000)])"
# 1000 loops, best of 5: 1.83 msec per loop
