names = ('Kamil', 'Mariusz', 'Dominik') #Niemutowalne - nie mozna dodać, ani odjąć elementu

print(names)

for name in names:
    print(name)

print(names[0])
print(names[1])
print(names[2])

# names.del /.append  - nie istnieją

#W krotkach często przechowywane są dane różnego typu:
user = ('Kamil', 35)
user1 = ('Dominik', 25)
user2 = ('Mariusz', 30)

users = [user, user1, user2]

for user in users:
    print(user)

