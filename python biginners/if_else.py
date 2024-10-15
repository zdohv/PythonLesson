""" условнфе выражения  (if-elif-else)"""


# bool() - неизменяемый тип данных, котрым имеет только два значения: true, false

# 10 > 2  True
# < - больше 
# <= - меньше или равно
# >= - болше или равно
# != - неравенство
# == - равенство

# print(23 == 25) false
# print(25.0 == 25) true
# print("яблоко" > 2) error 

# print(bool(0)) false
# print(bool(1)) true

# print(bool(2)) True
# print(bool(-2))True

# print(bool('it')) True
# print(bool(''))False

# bool({})False
# bool([])False
# bool(set())False
# bool(None)False


# """ if else """
# num = 15
# if num > 20:
#     print('num больше 20')
# else:
#     print('num НЕ больше 20')


# temp = 40

# if temp < 20:
#     print('холодно')
# else:
#     if temp < 30:
#         print('тепло')
#     else:
#         if temp > 35:
#             print('жарко')


""" elif """

# temp = 40
# if temp < 20:
#     print('холодно')
# elif temp < 30:
#     print('тепло')
# elif temp < 35:
#     print('жарко')
# else:
#     print('неверная пемпература')


# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# elif num2


# mark = input('введите отценку от 1 до 10')
# if mark.isdigit():
#     mark = int(mark)
#     msg = ''
#     if mark =='5':
#         msg = 'Ты молодец'
#     elif mark =='4':
#         msg = 'хорошо'
#     elif mark <= 3:
#         msg = 'потяни предмет'

#     print(msg)

# """ and, or, not """
# age = 14
# if age >= 18 and age < 28:
#     print('входит')
# else:
#     print('входа нет')


""" and, or, not """
# age = 18
# if age >= 18 and age < 28:
#     print('Входите')
# else:
#     print('Входа нет')

# False # False
# True # True
# False and False # False
# True and True # True
# False and True # False
# True and False # False

# False or False # False
# True or True # True
# False or True # True
# True or False # True

# not True # False
# not False # True

# (False or True) and (False and False) # False

""" is, ==, in """

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# print(a == b)


# string = 'hello world'
# print('world' in string)

# """ тернарный аператор """

# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     print('Сообщение длиннее 10')
# else:
#     print('Сообщение короче 10')

# msg = input('Введите сообщение ')

# res = 'сообшение длиннее 10' if len(msg) > 10 else 'сообшение короче 10'
# print(res)



