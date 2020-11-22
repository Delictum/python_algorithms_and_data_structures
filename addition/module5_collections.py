'''
from collections import Counter

a = Counter()
b = Counter('abracadabra')
c = Counter({'a': 1, 'b': 2})
d = Counter(cat=4, dog=6)

print(b)
b['z'] = -1

print(a, b, c, d, sep='\n')
print(b + c, b - c, b & c, b | c, +b, -b)
'''

'''
from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])

print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)

print(a, b, c, sep='\n')

print('*'*50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print('*'*50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print('*'*50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
print(g)
g.insert(2, 6)
print(g)

g.reverse()
print(g)

g.rotate(3)
print(g)
'''

'''
from collections import defaultdict


a = defaultdict()
print(a)

s = 'fsagsdgsdjfngjdghbjhasguyfgwytafbjkasdnvklmdslkbdf'
b = defaultdict(int)
for i in s:
    b[i] += 1
print(b)

list1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list1:
    c[k].append(v)
print(c)

list2 = [('cat', 1), ('dog', 5), ('cat', 2), ('cat', 1), ('dog', 1), ('dog', 5)]
d = defaultdict(set)
for k, v in list2:
    d[k].add(v)
print(d)

f = defaultdict(lambda: 'unknown')
f.update(rex='dog', tomas='cat')
print(f)
print(f['rex'], f['jerry'], sep='\n')
'''

'''
from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

b = {'cat': 5, 'dog': 2, 'mouse': 4}
new_b = OrderedDict(sorted(b.items(), key=lambda x: x[1]))
print(new_b)

print(new_a == new_b)

new_b.move_to_end('mouse')
print(new_b)
new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem()
print(new_b)
new_b.popitem(last=False)
print(new_b)

new_b['cow'] = 1
print(new_b)

new_b['dog'] = 8
print(new_b)
'''

'''
from collections import namedtuple

hero1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero1[4])


class Person:
    def __init__(self, name, race, health, mana, strength):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strength = strength


hero2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
hero3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero3.race)

prop = ['name', 'race', 'health', 'mana', 'strength']
New_Person1 = namedtuple('New_Person1', prop)
hero4 = New_Person1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero4.name)

print('*'*72)
Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

print('*'*72)

New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
p4 = New_Point(5)
print(p4)

print(p4._field_defaults)

dct = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Point(**dct)
print(p5)
'''


from collections import ChainMap


d1 = {'a': 2, 'b': 4, 'c': 6}
d2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d1, d2)
x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})
print(x)

print(x.maps[0], x.maps[-1])
print(x.parents)

y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y)

print(list(y))
print(list(y.values()))
