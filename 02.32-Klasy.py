#User
#name
#mail
#age

# user = ('Kamil', 'kamil@programujodpodstaw.pl', 35) #krotka

class User:
    def __init__(self, name, mail, age):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.mail)
        print(self.age)

    def is_male(self):
        return self.name[-1] != 'a'

# user = User() #Instancja klasy user
# user.name = 'Kamil'
# user.mail = 'kamil@programujodpodstaw.pl'
# user.age = 35
#
# user.print_info()
#
# user1 = User() #Instancja klasy user
# user1.name = 'Mariusz'
# user1.mail = 'mariusz@mariusz.pl'
# user1.age = 25
#
# user1.print_info()
#
# print(user.name)
# print(user.age)

user = User('Kamil', 'kamil@programujodpodstaw.pl', 35)
user1 = User('Paulina', 'kamil@programujodpodstaw.pl', 35)
user.print_info()
print(user.is_male())
print(user1.is_male())