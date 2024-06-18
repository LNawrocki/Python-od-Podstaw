# import datetime
from datetime import datetime, timedelta

# date1 = datetime.datetime(2024, 4, 8)
# date2 = datetime.datetime(2024, 4, 4)
date1 = datetime(2024, 4, 8)
date2 = datetime(2024, 4, 4)

print(date1 - date2)
print(date2 - date1)

print(date1)
date1 += timedelta(30)
print(date1)
