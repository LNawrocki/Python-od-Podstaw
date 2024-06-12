countries_information = {}

countries_information['Polska'] = ('Warszawa', 38)
countries_information['Niemcy'] = ('Berlin', 86)
countries_information['Francja'] = ('Paryż', 57)

def print_country_information(country):
    print('Kraj: ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkańców (mln): ' + str(countries_information[country][1]))


print_country_information('Niemcy')
print()
print_country_information('Francja')
print()
print_country_information('Polska')


