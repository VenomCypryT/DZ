# задание 1:
# def num (a, b):
#     try:
#         a, b = int(a), int(b)
#         res = a / b
#     except ZeroDivisionError:
#         return "делить на ноль нельзя"
#     return res
#
# a = input('введи число 1:')
# b = input('введи число 2:')
#
# print(num(a, b))

# задание 2
# def data(name, female, age, sity, email, telephon):
#     print(f'{name}, {female}, {age}, {sity}, {email}, {telephon}')
# data(input('Enter name:'), input('Enter female:'), input('Enter age:'), input('Enter sity:'), input('Enter email:'), input('Enter telephon:'))

# задание 3
# def min(a, b, c):
#     try:
#         res = sum(sorted([a, b, c])[1:])
#         return res
#     except TypeError:
#         return 'Не число'
# print(min(20, 98, 50))

# задание 4
# def num(x, y):
#     try:
#         res = x ** y
#         return res
#     except TypeError:
#         return 'Не цифра'
# print(num(5, -2))

# задание 5
# def num():
#     res = 0
#     while True:
#         li = input('введи число через пробел, для выхода -stop:').split()
#         for num in li:
#             if num.lower() == 'stop':
#                 return res
#             else:
#                 try:
#                     res += int(num)
#                 except ValueError:
#                     return 'Для выхода - stop'
#         print('Summa = ', res)
# print(num())

# задание 6
# def num():
#     li = input('Введите слова через пробел:  ').split()
#     for word in li:
#         lenn = 0
#         for ch in word:
#             if 97<= ord(ch) <= 122:
#                 lenn += 1
#         if lenn == len(word):
#             print(word.title())
#         else:
#             print(f'Ошибка: {word} - можно вводить только нижний регистр')
# num()