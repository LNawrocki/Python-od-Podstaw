# names = []
# print(names)
#
# names2 = ['Kamil', 'Mariusz']
# print(names2)
#
names3 = ['Kamil', 'Mariusz', 2]
names3.append('Dominik') #Dodaje pojedynczy element czyli np listę names3.append(['Paulina', Rafał])
#elementy na liście mogą być różnego typu np. imiona i listy imion
# print(names3)
#
# print(names3[2])
#
# for name in names3:
#     print(name)
#
#
# del names3[1]
# print(names3)
#
# names3.remove('Kamil') #usuwa pierwsze wystąpienie
# print(names3)
#
# print(len(names2))

# names3.sort(reverse=True)
# print(names3)

names3.extend(['Paulina', "Rafał"]) # Dodaje elementy jako osobne elementy istniejacej listy
print(names3)

names3[1] = "Adam"
print(names3)