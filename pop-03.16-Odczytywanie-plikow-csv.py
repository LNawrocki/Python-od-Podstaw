import csv

# with open('server_log.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     for row in csv_reader:
#         print(row[3])

# zamiana przecinków na średniki powoduje błąd

with open('server_log_semicoln.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        print(row[0])