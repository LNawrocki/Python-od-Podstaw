import csv

# with open('users_writer.csv', 'w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=';')
#     csv_writer.writerow(['Kamil', 35])
#     csv_writer.writerow(['Mariusz', 30])
#     csv_writer.writerow(['Dominik', 25])

# Z wierszem nagłówkowym

with open('users_writer.csv', 'w') as csv_file:
    fieldnames = ['name', 'age']
    csv_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Kamil', 'age': 35})
    csv_writer.writerow({
        'name': 'Mariusz',
        'age': 30
    })
    csv_writer.writerow({
        'name': 'Domimik',
        'age': 25
    })
