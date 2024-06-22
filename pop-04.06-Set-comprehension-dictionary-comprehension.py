names = ['Kamil', 'Mariusz', 'Domiki', 'Paulina', 'Asia', 'Kamil', 'Mariusz', 'Kamil']
# Set nie ma duplikatów
names2 = {name for name in names}
#Brak kolejności
print(names2)

numbers = [pow(number,2) for number in range(1, 11)]
print(numbers)

# Słownik klucz - wartość
numbers = {number: pow(number,2) for number in range(1, 11)}
print(numbers)

