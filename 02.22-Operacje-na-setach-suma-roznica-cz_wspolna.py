names = {'Kamil', 'Mariusz', 'Dominik', 'Rafał', 'Artur'}
names2 = {'Kamil', 'Paulina', 'Asia', 'Rafał'}

print(names)
print(names2)


# #Suma zbiorów - union
# print(names.union(names2))
# print(names | names2)
#
#
# #cześć wspólna
# print(names.intersection(names2))
# print(names & names2)

# Różnica - difference
# print(names.difference(names2))
# print(names - names2)
# print(names2 - names)

#Symetryczna różnica - symmetric difference
print(names.symmetric_difference(names2))
print(names ^ names2)