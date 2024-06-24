import random


# numbers = [random.randint(1, 10) for _ in range(10)]
# print(numbers)
#
# numbers2 = [num for num in numbers if num > 5]
# print(numbers2)

numbers = [num for _ in range(10) if (num := random.randint(1, 10)) > 5]
print(numbers)
