import shelve
from person import Person
from manager import Manager

'''
tom = Manager('Tom Jones', 50000)
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)

db = shelve.open('person_db')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()
'''

db = shelve.open('person_db')
for key in sorted(db):
    print(key, '=>', db[key])
