names = ['Kamil', 'Mariusz', 'Domiki', 'Paulina', 'Asia']
names2 = []


# for name in names:
#     if name.endswith('a'):
#         names2.append(name)

# names2 = [name.upper() for name in names if name.endswith('a')]
# names2 = [name.upper() if name.endswith('a') else name.lower() for name in names]
# na końcu filtrownanie elementów, a na początku wykonujemy operacje na odfiltrowanych elementach
names2 = [name.upper() if name.endswith('a') else name.lower() for name in names if len(name) > 5]

print(names2)