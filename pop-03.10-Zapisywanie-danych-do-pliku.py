# 'w' nadpisuje cały plik
# 'a' dopisywanie
with open('test.txt', 'a') as file:
    file.write("Mariusz\n")