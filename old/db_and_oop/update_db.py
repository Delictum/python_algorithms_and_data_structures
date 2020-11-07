import shelve


db = shelve.open('person_db')

for key in sorted(db):
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.give_raise(.10)
db['Sue Jones'] = sue

db.close()
