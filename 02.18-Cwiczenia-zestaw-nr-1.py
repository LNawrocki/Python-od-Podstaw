# 1. Napisz program, który sprawdza, czy podana przez użytkownika liczba jest parzysta czy nieparzysta
#
# 2. Napisz program, który sprawdxa, czy podana przez użtykownika liczba jest większa od zera, mniejsza od 0, róena 0
#
# 3. Napisz program, który zapyta użytkoenika o wynik na egzaminie (od 0 do 100) i wyświetli osdpowidnią ocenę:
# 90-100 -> 5
# 80-89 _> 4
# 70-79 -> 3
# 60-69 -> 2
# poniżej 60 -> 1
#
# 4. Napisz program, który wyświetli liczby od 0 do 100
#
# 5. Napisz program, który wyświetli wszystkie liczby pierwsze od 1 do 100
#
# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych z przedziału 1 - 100
#
# 7. Napisz program, który policzy pole prostokąta
# (użytkonik musi podać długości boków)
#
# 8. Napisz program, który sprawdzi, czy podane imię jest męskie czy żeński (założenie - żeńskie kończą się na a)
#
# 9. Pobierz od użytkownika trzy liczby całkowite i uporządkuj je w kolejności od najmniejszej do największej
#
# 10. Stwórz grę, w której wylosujesz liczbę z przedziału 1 - 100, zapiszesz ją do zmiennej, a następnie poprosisz użytkownika o odgadnięcie tej liczby.
# Po każdej próbie wyświetl informację czy liczba podana przez użytkownika jest mniejsza czy większa od wylosowanej. Gdy użytkownika odgadnie liczbę, zakończ grę.
# Sprawdź jak losować liczby całkowie w Pythonie


#1
# number = int(input("Podaj liczbę do sprawdzenia czy jest parzysta: "))
#
# if (number % 2) == 0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba nie jest parzysta")

###################################################

#2
# number = int(input("Podaj liczbę do sprawdzenia: "))
#
# if number > 0:
#     print("Liczba jest większa od zera")
# elif number < 0:
#     print("Liczba jest mniejsza od zera")
# else:
#     print("Liczba równa zero")

###################################################
#3
# while True:
#     number = int(input("Podaj liczbę punktów: "))
#     match number:
#         case _ if number >= 90:
#             print("Ocena 5")
#         case _ if 80 <= number <= 89:
#             print("Ocena 4")
#         case _ if 70 <= number <= 79:
#             print("Ocena 3")
#         case _ if 60 <= number <= 69:
#             print("Ocena 2")
#         case _:
#             print("Ocena 1")

###################################################

#4
# for number in range(1, 101):
#     print(number)

###################################################

#5

###################################################

#6
# sum = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         sum += number
# print(sum)

###################################################

#7
# dimA = int(input("Podaj pierwszy bok (cm): "))
# dimB = int(input("Podaj drugi bok (cm): "))
#
# print(f"Pole prostokąta wynosi {dimA * dimB}cm")

###################################################

#8
# name = input("Podaj imie: ")
#
# if name.endswith("a"):
#     print("Podałeś imie żeńskie")
# else:
#     print("Podałeś imie męskie")
#

###################################################

#9
# print("Podaj 3 liczby - uporządkuję je narastająco.")
#
# num1 = int(input("Podaj pierwszą liczbę: "))
# num2 = int(input("Podaj drugą liczbę: "))
# num3 = int(input("Podaj trzecią liczbę: "))

###################################################

#10


