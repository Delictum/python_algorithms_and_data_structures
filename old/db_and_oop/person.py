'''
Класс Person для исполнения ряда обыденных задач
'''

from classtools import AttrDisplay


class Person(AttrDisplay):
    '''
Создает и обрабатывает записи с информацией о людях
    '''
    def __init__(self: 'объект', name: 'имя', job: 'работа'=None,
                 pay: 'оплата'=0) -> 'object Person':
        '''
Конструктор принимает имя, работу и оплату. Параметр name является обязательным.
        '''
        self.name = name
        self.job = job
        self.pay = pay

    def get_last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob)
    print(sue)
    print(Person.__init__.__annotations__)
    print(Person.__init__.__doc__)
    print(bob.get_last_name(), sue.get_last_name())
    sue.give_raise(.10)
    print(sue.pay)
    print(help(Person.__init__))
        
