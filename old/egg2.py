# put your python code here

import sys
sys.stdin = open("input.txt", "r")


n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]
print(parents)

def is_parent(e, exceptions):
    global p
    if e in parents and len(parents[e]) != 0:
        for i in parents[e]:
            #print(p)
            if i in exceptions:
                p.append(True)
            else:
                p.append(False)
                is_parent(i, exceptions)
            
    return False

 

exceptions = []
q = int(input())
for _ in range(q):
    e = input()
    exceptions.append(e)
    p = []
    if exceptions.count(e) != 1 or is_parent(e, exceptions) or True in p:
        print(e)
        pass
    #print(p)

