'''
timer(spam, 1, 2, a=3, b=4, _reps=1000) вызывает и измеряет время работы функции
spam(1, 2, a=3) _reps раз, и возвращает общее время, затраченное на все вызовы,
с результатом вызова испытуемой функции;

best(spam, 1, 2, a=3, b=4, _reps=50) многократно вызывает функцию timer, чтобы
исключить влияние флуктаций в нагрузке на систему, и возвращает лучший результат
из серии по _reps испытаниям.
'''

import sys
import time


trace = lambda *args: None
timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs, _reps)
    
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret, )

def best(func, *pargs, **kargs):
    best_result = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best_result:
            best_result = time
    return (best_result, ret, )
