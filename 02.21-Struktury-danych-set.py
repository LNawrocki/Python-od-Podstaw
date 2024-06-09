names = {'Kamil', 'Mariusz', 'Dominik'}
print(names)

names = {'Kamil', 'Mariusz', 'Dominik', 'Mariusz'} #SET - nie ma duplikatów, kolejnośćjest losowa
print(names)

names.add('Rafał')
print(names)

names = {'Kamil', 'Mariusz', 'Dominik'}
names.remove('Mariusz')
print(names)

for name in names:
    print(name)

names.update({"Łukasz", 'Bartek'})
names.update(["Jola", 'Franek'])
print(names)