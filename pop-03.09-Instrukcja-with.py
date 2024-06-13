# With statment zadba o zamkniecie pliku niezależnie od wyjątków i błędów
try:
    with open('test.txt') as file:
        # file_content = file.read()
        # print(file_content)

        # print(file.readline())
        # print(file.readline())
        # print(file.readline())
        # print(file.readline())
        # print(file.readline())
        # print(file.readline())

        # testowa linia
        #
        # druga linia
        #
        # trzecia linia
        #
        #
        #
        # Kamil
        #
        # Mariusz

        # print(file.readlines())
        # ['testowa linia\n', 'druga linia\n', 'trzecia linia\n', '\n', 'Kamil\n', 'Mariusz\n', 'Dominik']

        # wczytanie całego pliku
        # for line in file.readlines():
        #     print(line)

        # czytanie wiersz po wierszu
        for line in file:
            print(line)

except FileNotFoundError:
    print("Plik nie został znaleziony")
