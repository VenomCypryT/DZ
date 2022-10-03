# 1 задание
# from sys import argv
#
# def money():
#     try:
#         hours, rate, premium = map(float, argv[1:])
#         print('Зарплата', hours * rate + premium)
#     except ValueError:
#         print('Запустить скрипт с трем параметрами')
#
# money()

# 2 задание
# li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
# print(new)

# 3 задание
# new = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
# print(new)

# 4 задание
# li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new = [i for i in li if li.count(i) == 1]
# print(new)

# 5 задание
# from functools import reduce
#
# new = [i for i in range(99, 1001) if i % 2 == 0]
# print(new)
# sum_all = reduce(lambda a, b : a * b, new)
#
# print(sum_all)

# 6 задание
# from itertools import count, cycle
# st = int(input('введите начальное число:  '))
# end = int(input('Введите конечное число'))
#
# for el in count(st):
#     print(el)
#     if el == end:
#         break

# 7 задание

# def function(b):
#     res = 1
#     if b == 0:
#         yield f'{b}! = 1'
#     for i in range(1, b + 1):
#         res *= i
#         yield f'{i}! = {res}'
#
# n = int(input('Введите число,. факториал которого хотите получить: '))
# for el in function(n):
#     print(el)