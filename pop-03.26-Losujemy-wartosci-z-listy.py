import random

names = ['Kamil', 'Mariusz', 'Dominik']

print(random.choice(names))
# wagi okreslają jak często dana wartość będzie losowana
print(random.choices(names, k=5, weights=[2, 1, 1]))
# wagi skumuowane dają w rezultacie [2, 3, 4]
print(random.choices(names, k=5, cum_weights=[2, 1, 1]))
# losowanie 2 różnych wartości
print(random.sample(names, 2))

print(names)
random.shuffle(names)
print(names)