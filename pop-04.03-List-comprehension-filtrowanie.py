names = ['Kamil', 'Mariusz', 'Domiki', 'Paulina', 'Asia']
names2 = []


# for name in names:
#     if name.endswith('a'):
#         names2.append(name)

names2 = [name.upper() for name in names if name.endswith('a')]
print(names2)