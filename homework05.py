from datetime import date


class Contact:
    def __init__(self, id, first_name, last_name, birth_date, profession):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.profession = profession
    def get_information (self):
        print(f'ID - {self.id}')
        print(f'Full name - {self.last_name} {self.first_name}')
        print(f'Birth date - {self.birth_date}')
        print(f'Profession - {self.profession}')

c = Contact(id=1,
first_name='John',
last_name='Dow',
birth_date=date(day=21, month=4, year=1996),
profession='Python developer')
c.get_information()

class Bird:
    def __init__(self, type, age, meal, canFly, canSwim):
        self.type = type
        self.age = age
        self.meal = meal
        self.canFly = canFly
        self.canSwim = canSwim
    def can_fly(self):
        if self.canFly:
            print('I can fly')
        else:
            print('I can not fly')
    def can_swim(self):
        if self.canSwim:
            print('I can swim')
        else:
            print('I can not swim')
    def eat(self):
        print(f'I eat {self.meal}')

class Fish:
    def __init__(self, type, age, meal, canFly, canSwim):
        self.type = type
        self.age = age
        self.meal = meal
        self.canFly = canFly
        self.canSwim = canSwim
    def can_fly(self):
        if self.canFly:
            print('I can fly')
        else:
            print('I can not fly')
    def can_swim(self):
        if self.canSwim:
            print('I can swim')
        else:
            print('I can not swim')
    def eat(self):
        print(f'I eat {self.meal}')

class Mammal:
    def __init__(self, type, age, meal, canFly, canSwim):
        self.type = type
        self.age = age
        self.meal = meal
        self.canFly = canFly
        self.canSwim = canSwim
    def can_fly(self):
        if self.canFly:
            print('I can fly')
        else:
            print('I can not fly')
    def can_swim(self):
        if self.canSwim:
            print('I can swim')
        else:
            print('I can not swim')
    def eat(self):
        print(f'I eat {self.meal}')

class Falcon(Bird):
    def whoAmI(self):
        print(f'I am - {self.type} and {self.age} years old')
class Penguin(Bird):
    def whoAmI(self):
        print(f'I am - {self.type} and {self.age} years old')

class Forel(Fish):
    def whoAmI(self):
        print(f'I am - {self.type} and {self.age} years old')

class Whale(Mammal):
    def whoAmI(self):
        print(f'I am - {self.type} and {self.age} years old')


f = Falcon(type ='Falcon', age = 2, meal='meat', canFly=True, canSwim=False)
f.whoAmI()
f.can_fly()
f.can_swim()
f.eat()

p = Penguin(type ='Penguin', age = 1, meal='fish', canFly=False, canSwim=True)
p.whoAmI()
p.can_fly()
p.can_swim()
p.eat()

Fo = Forel(type ='Forel', age = 3, meal='insects', canFly=False, canSwim=True)
Fo.whoAmI()
Fo.can_fly()
Fo.can_swim()
Fo.eat()

W = Whale(type ='Whale', age = 12, meal='fish', canFly=False, canSwim=True)
W.whoAmI()
W.can_fly()
W.can_swim()
W.eat()


# test