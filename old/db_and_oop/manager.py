from person import Person


class Manager(Person):
    '''
Версия класса Person, адаптированная в соответствии
со специальными требованиями
    '''
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)
        
    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raise(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.get_last_name())
    print(tom)

    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(Person.__init__.__annotations__)
    print(Person.__init__.__doc__)
    print(bob.get_last_name(), sue.get_last_name())
    sue.give_raise(.10)
    print(sue.pay)
    
    print('--All three--')
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)

    print('--Create department--')
    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raise(.10)
    development.show_all()
    print(help(Manager))
    print(help(Manager))
