def divide(a, b):
    return a / b


try:
    a = int(input("Podaj pierwszą liczbę:"))
    b = int(input("Podaj drugą liczbę:"))
    print(divide(a, b))
except ZeroDivisionError:
    print("Nie mozna dzielić przez zero!")
except ValueError:
    print("podałeś niewłasciwą liczbę!")
finally:
    print("To wykona się zawsze")

print('Koniec programu')