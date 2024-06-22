import os

print(os.getcwd())

current_directory = os.getcwd()
print(current_directory)
print(os.listdir(current_directory))


new_directory = os.path.join(current_directory, 'test_directory')
# ścieżka relatywna
# new_directory = os.path.join('./', 'test_directory')
# new_directory = os.path.join('test_directory') - aktualny katalog

os.mkdir(new_directory)
print(os.listdir(current_directory))
# Odnosząc się do bierzącej lokalizacji możemy pominąć agtument
# print(os.listdir())

os.rmdir(new_directory)
print(os.listdir())


print(os.path.exists('.venv'))
print(os.path.isdir('.venv'))
print(os.path.isfile('.venv'))

print(os.getcwd())

path = 'C:/kurs/Python_od_podstaw/nowy'
with open(os.path.join(path, 'test.txt'), 'x'):
    pass