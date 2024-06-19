from collections import Counter, namedtuple

# person = ('Kamil', 36)
# print(person[0])

Person  = namedtuple('Person', ['name', 'age'])

# krotka dla pól też OK.
# Person  = namedtuple('Person', ('name', 'age'))

person = Person(name='Kamil', age=36)
print(person)

person1 = Person(age=36, name='Kamil')
print(person1)
print(person1.age)
print(person1.name)
