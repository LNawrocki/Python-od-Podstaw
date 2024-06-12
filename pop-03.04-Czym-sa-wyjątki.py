# Błąd składni
# if True:
# print('ok')
# IndentationError: expected an indented block after 'if' statement on line 1


# Błędy logiczne - Wyjątki
def divide(a, b):
    return a / b


# print(divide(1, 0))
# ZeroDivisionError: division by zero

try:
    print(divide(1, 0))
except:
    print("Nie mozna dzielić przez zero")

