class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def showFIelds(self):
        print(f'Animal: {self.name}, Age: {self.age} years old, Weight: {self.weight} kg')


dog = Animal("Dog", 5, 7)
dog.showFIelds()


class Monkey:
    max_age = 12
    loves_bananas = True
    def __init__(self, max_age, loves_bananas):
        self.max_age = max_age
        self.loves_bananas = loves_bananas
    def climb(self):
        print('I am climbing the tree')
    def showFields(self):
        print(f'Max age is: {self.max_age}, Monkey love bananas?: {self.loves_bananas}')

gorilla = Monkey(20, False)
gorilla.showFields()
gorilla.climb()

marmoset = Monkey(2, True)
marmoset.showFields()
marmoset.climb()


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def calculate_age(self, nextAge):
        print(f'Через {nextAge} лет {self.name} исполнится {self.age + nextAge}')


person = Person("Kate", 20, "female")
person.calculate_age(5)