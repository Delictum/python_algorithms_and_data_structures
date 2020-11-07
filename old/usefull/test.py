import sys
import speed_tester


reps = 10000
reps_list = range(reps)


def for_loop():
    res = []
    for x in reps_list:
        res.append(abs(x))
    return res

def list_comp():
    return [abs(x) for x in reps_list]

def map_call():
    return list(map(abs, reps_list))

def gen_expr():
    return list(abs(x) for x in reps_list)

def gen_func():
    def gen():
        for x in reps_list:
            yield abs(x)
    return list(gen())


print(sys.version)
for tester in (speed_tester.timer, speed_tester.best):
    print('<%s>' % tester.__name__)
    for test in (for_loop, list_comp, map_call, gen_expr, gen_func):
        elapsed, result = speed_tester.timer(test)
        print('-'*33)
        print('%-9s: %.5f => [%s...%s]' %
              (test.__name__, elapsed, result[0], result[-1]))
