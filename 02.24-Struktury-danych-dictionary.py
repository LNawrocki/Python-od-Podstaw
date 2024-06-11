#słownik - klucz wartość

phone_book = {
    'Kamil': 100200300,
    'Mariusz': 33889832,
    'Dominik': 666777888,
    'Kamil': 3333333
}

# print(phone_book)

# print(phone_book.get('Dominik')) #
# print(phone_book['Dominik'])

# phone_book["Kamil"] = 777777777

print(phone_book)

#Przy del mamy tylko informacje o błędzie
# del phone_book['Mariusz']
# print(phone_book)

#pop zwraca wartość usuniętego klucza,
# jeśli klucz nie istnieje, można zwrócić domyslną wartość (np.-1 )
deleted_phone_number = phone_book.pop('Mariusz123', "Brak numeru")

print(deleted_phone_number)
print(phone_book)

for element in phone_book:  #Zwraca klucze
    print(element)

for element in phone_book.values():  #Zwraca wartości
    print(element)

for element in phone_book.keys():  #Zwraca klucze
    print(element)

for element in phone_book.items():  #Zwraca krotki (tuple)
    print(element)

for element in phone_book.items():  #Zwraca krotki (tuple)
    print(element[0] + ":" + str(element[1]))

for name, phone_number in phone_book.items():  #Zwraca krotki (tuple)
    print(name + ":" + str(phone_number))