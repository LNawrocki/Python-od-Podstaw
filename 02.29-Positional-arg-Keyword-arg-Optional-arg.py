def hello_1(name, age, last_name='DEFAULT'): #Paramerty opcjonalne muszą być po parametrach wymaganych
    print('Cześć ' + name + '! Masz ' + str(age) + ' lat.')
    print('Masz na nazwisko ' + last_name)


def hello_2(name, age, last_name=None):
    print('Cześć ' + name + '! Masz ' + str(age) + ' lat.')
    if last_name is not None:
        print('Masz na nazwisko ' + last_name)


hello_1("Wojtek", 10, 'Nawro') #Positional arguments

hello_1(age=25, name='Lukas') #Keyword arguments
hello_1(age=25, name='Lukas', last_name='Nawro') #Keyword arguments

hello_1(age=25, name='Lukas', last_name='New') #Optiona paramert - DEFAULT i definition

print()
hello_2('Luk', 40)
hello_2('luk', 40, 'naw')