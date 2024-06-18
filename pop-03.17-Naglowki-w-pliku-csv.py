import csv

with open('server_log_headers.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # print(row['status_code'])
        print(row['ip'])