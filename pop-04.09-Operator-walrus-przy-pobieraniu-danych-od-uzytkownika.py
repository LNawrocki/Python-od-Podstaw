# expenses = []
# expense = None
#
# while expense != 0:
#     expense = int(input("Dodaj wydatek(podaj 0, by zakończyć"))
#     if expense >0:
#         expenses.append(expense)
#
# print(expenses)
# print(sum(expenses))

expenses =[]

while(expens := int(input("Dodaj wydatek(podaj 0, by zakończyć"))) != 0:
    expenses.append(expens)

print(expenses)
print(sum(expenses))
