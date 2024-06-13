# w Trybie r+ zapisujemy w miejscu kursora i nadpisujemy
with open('test.txt', 'r+') as file:
    file.seek(0,2) # 2 - koniec pliku
    file.write("Luki\n")
    file.seek(0)
    print(file.read())
