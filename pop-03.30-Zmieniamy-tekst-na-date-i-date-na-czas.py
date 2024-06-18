from datetime import datetime, timedelta

# now = datetime.now()
# print(now)

# now_string = now.strftime("%d:%m:%Y %H:%M:%S")
# now_string = now.strftime("%d/%m/%Y %H/%M/%S")
# print(now_string)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# string to date
# date_string = '01.04.2024'
# date_obj = datetime.strptime(date_string,"%d.%m.%Y")

date_string = '01/04/2024'
date_obj = datetime.strptime(date_string,"%d/%m/%Y")
print(date_obj)


