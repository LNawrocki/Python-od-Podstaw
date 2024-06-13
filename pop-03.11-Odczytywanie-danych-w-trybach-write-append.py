# 'w' nadpisuje cały plik
# 'a' dopisywanie
# with open('test.txt', 'a') as file:
#     file.write("Kamil\n")
#     file.write("Mariusz\n")
#     file.write("Dominik\n")
#     file.seek(0)
#     print(file.read())

# 'w+, a+' dodatkowo odczytuje

with open('test.txt', 'a+') as file:
    file.write("Adam\n")
    file.seek(0)
    print(file.read())