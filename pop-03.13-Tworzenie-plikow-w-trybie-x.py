# w Trybie x - jeśli plik nie istnieje, jesli istnieje to wyjątek
with open('test2.txt', 'x') as file:
    file.write("Luki\n")

