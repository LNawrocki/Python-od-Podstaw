from datetime import datetime
import locale

# date_string = '01 April 2024'
# date_obj = datetime.strptime(date_string, "%d %B %Y")
# # %B dla EN
# print(date_obj)


locale.setlocale(locale.LC_TIME, "pl_PL")
date_string = '01 kwietnia 2024'
date_obj = datetime.strptime(date_string, "%d %B %Y")
# %B dla EN
print(date_obj)
