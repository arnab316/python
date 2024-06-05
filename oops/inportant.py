class Person:
    name = 'annonymous'
    height = '5.6'
    @classmethod
    def changeName(cls ,name):
           cls.name = name



p1 = Person()
p1.changeName('Arnab')
print(p1.name)
# print(Person.name)