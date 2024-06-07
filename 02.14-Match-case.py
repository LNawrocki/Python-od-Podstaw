# light = input("Jakie jest światło? (zielone, żółte, czerwone)")
#
# if light == 'zielone':
#     print("Mozesz jechać")
# elif light == 'żółte':
#     print("Przygotuj się")
# elif light == 'czerwone':
#     print('Stój')
# else: print("Niewłaściwy kolor")


light = input("Jakie widzisz światło? (zielone, żółte, czerwone")

match light:
    case 'zielone':
        print("Możesz jechać")
    case 'żółte':
        print("Przygotuj się")
    case 'czerwone':
        print("Stókj!")
    case _:
        print("Nie znam takiego koloru")