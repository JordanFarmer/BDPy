age = 38
print(hex(id(age)))
age = 39
print(hex(id(age)))


class Person(object):
    def __init__(self, age):
        self.age = age

person1 = Person(38)
print('before assignment, person1 id=%s'%(hex(id(person1))))
print('when age=38, person1.age id=%s'%(hex(id(person1.age))))
person1.age = 39
print('after assignment, person1 id=%s'%(hex(id(person1))))
print('when age=39, person1.age id=%s'%(hex(id(person1.age))))