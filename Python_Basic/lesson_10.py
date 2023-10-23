# import random
# import math
# # from random import *
# # from random import randint, choice

# print(random.randint(1, 100)) # від 1 до 100
# print(random.random())
# print(random.choice("qwerty"))
# print(random.randrange(10)) # від нуля до 9
# print(random.randrange(2, 10)) # від 2 до 9
# print(random.randrange(2, 10, 2)) # від 2 до 9 через один (кожен другий)
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums) # перемішуємо значення списку
# print(nums)

##########
##
# print(-math.inf)
# print(math.inf)
# print(math.ceil(10.2))
# print(math.floor(10.999))
# print(math.factorial(5))
# print(math.pow(2, 3))
# print(math.sqrt(9))

#############
##
# from decimal import *
#
# number = 0.1 + 0.1 + 0.1
# print(number)
# number = Decimal("0.1")
# number = number + number + number
# print(number)
# #
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.00"))
# print(number)
# #
# number = Decimal("0.333")
# number = number.quantize(Decimal("1.0000"))
# print(number)
#
# number = Decimal("12.123456789")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.5555")
# number = number.quantize(Decimal("1.000"))
# print(number)
#
# number = Decimal("12.9999")
# number = number.quantize(Decimal("1.000"))
# print(number)
# #
# # округлення відбувається до найближчого парного числа, якщо округлена частина дорівнює 5
# number = Decimal("12.025")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.035")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)
#
# number = Decimal("12.026")
# number = number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)
# print(number)

##################
# datetime
# import datetime as dt

# print(dt.date.today())
# print(dt.date(2022, 11, 10))
# print(dt.time())
# print(dt.time(10, 13, 15))
# print(dt.time(10, 13))
# #
# print(dt.datetime.now())
# dt_now = dt.datetime.now()
# print(f"{dt_now.day}/{dt_now.month}/{dt_now.year} {dt_now.hour}:{dt_now.minute}:{dt_now.second}:{dt_now.microsecond}")
# #
# print(dt.datetime)
# #
# my_date = dt.datetime.strptime("12/03/2020", "%d/%m/%Y")
# print(my_date)

# https://www.programiz.com/python-programming/datetime/strftime

# from datetime import datetime, timezone, timedelta
#
# # naive
# naive = datetime.now()
# print("Naive DateTime:", naive)
#
# # UTC aware
# UTC = datetime.now(timezone.utc)
# print("UTC DateTime", UTC)
#
# # Creating a datetime with JST (Japan) TimeZone
# jst_dateTime = datetime.now(timezone(timedelta(hours=+9), 'JST'))
# print("In JST::", jst_dateTime)

###############
# Генератори колекцій
# list comprehension

# newlist = [expression for item in iterable (if condition)]

# iterable: джерело даних, що перебирається, в якості якого може виступати список, безліч, послідовність,
# або навіть функція, яка повертає набір даних, наприклад, range()
#
# item: елемент, що витягується з джерела даних
#
# expression: вираз, який повертає певне значення. Це значення потім потрапляє в список, що генерується
#
# condition: умова, якій повинні відповідати елементи, що витягуються з джерела даних.
# Якщо елемент НЕ задовольняє умову, він не вибирається. Необов'язковий параметр.

# # v1
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive = []
# for num in numbers:
#     if num > 0:
#         numbers_positive.append(num)
#
# print(numbers_positive)
# #
# # # v2
# numbers_positive_2 = [num for num in numbers if num > 0]
# print(numbers_positive_2)
#
# #
# nums = [n for n in range(10)]
# print(nums)
#
# #
# nums = [n for n in range(10) if n % 2 == 0]
# print(nums)
#
# #
# users = {1: 'John', 2: 'Peter', 3: 'Max'}
# names = [name for name in users.values()]
# print(names)
#
# #
# users_data = [f"{key}: {users[key]}" for key in users.keys() if key > 2]
# print(users_data)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# numbers_positive_2 = tuple([num * 2 for num in numbers if num > 0])
# print(numbers_positive_2)
#
# #
# numbers = [-1, 2, -3, 4, -5, 6, -7, 7]
# new_numbers = [num * 2 if num > 5 else num for num in numbers if num > 0]
# print(new_numbers)
#
# # #
# my_dict = {i: i ** 2 for i in range(10)}
# print(my_dict)
#
# #
# my_set = {i for i in range(10)}
# print(my_set)

##################
# Генераторні функції
# Генератор - це об'єкт, який відразу при створенні не обчислює значення всіх своїх елементів
# generator = (i for i in range(3))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # StopIteration
# close() -> зупинка генератора
# throw() -> генератор кине виняток

# for i in generator:
#     print(i)
#
#
# def create_generator():
#     number = 1
#     while True:
#         yield number
#         number += 1
#
#
# my_gen = create_generator()
# print(my_gen)
# try:
#     for i in my_gen:
#         print(i)
#         if i > 10:
#             my_gen.close()
#             # my_gen.throw(Exception("End!"))
# except Exception as e:
#     print(e)

########
# def demo_gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
#
# my_gen = demo_gen()
# for i in my_gen:
#     print(i)

######################
###########
# \d - відповідає будь-якій одній цифрі і замінює собою вираз [0-9];
# \D - виключає всі цифри та замінює [^0-9];
# \w - Замінює будь-яку цифру, букву, а також знак нижнього підкреслення;
# \W - будь-який символ крім латиниці, цифр або нижнього підкреслення;
# \s - відповідає будь-якому пробельного символу;
# \S - описує будь-який непробільний символ.
#
#
# . Один символ, крім нового рядка \n.
# ? 0 або 1 входження шаблону зліва
# + 1 і більше входжень шаблону зліва
# * 0 і більше входжень шаблону зліва
# \w Будь-яка цифра або буква (\W - все, крім букви або цифри)
# \d Будь-яка цифра [0-9] (\D - все, крім цифри)
# \s Будь-який символ пробілу (\S - будь-який символ пробілу)
# \b Кордон слова
# [..] Один із символів у дужках ([^..] — будь-який символ, крім тих, що у дужках)
# \ Екранування спеціальних символів (\. означає точку або \+ - знак "плюс")
# ^ і $ Початок і кінець рядка відповідно
# {n,m} Від n до m входжень ({,m} - від 0 до m)
# a|b Відповідає a або b
# () Групує вираз і повертає знайдений текст
# \t, \n, \r Символ табуляції, нового рядка та повернення каретки відповідно
#
# Для чого використовуються регулярні вирази
# для визначення потрібного формату, наприклад, телефонного номера або email-адреси;
# для розбивки рядків на підрядки;
# для пошуку, заміни та вилучення символів;
# для швидкого виконання нетривіальних операцій.
#
# А ось найбільш популярні методи, які надає модуль:
#
# re.match() - Цей метод шукає за заданим шаблоном на початку рядка
# re.search() - Метод схожий на match(), але шукає не лише на початку рядка
# re.findall() - Повертає список усіх знайдених збігів.
# У методу findall() немає обмежень на пошук на початку або в кінці рядка.
# re.split() - Цей метод поділяє рядок за заданим шаблоном
# re.sub() - Шукає шаблон у рядку і замінює його на вказаний підрядок.
# Якщо шаблон не знайдено, рядок залишається незмінним
# re.compile() - Ми можемо зібрати регулярне вираження в окремий об'єкт, який можна використовувати для пошуку.
# Це також позбавляє переписування одного і того ж виразу.

import re

# result = re.match(r'he', 'hello world hello')
# print(result)
# print(result.group(0))
#
#
# result = re.search(r'world', 'hello world hello')
# print(result.start())
# print(result.end())
#
#
# result = re.findall(r'he', 'hello world hello')
# print(result)
# #
# #
# result = re.split(r'l', 'hello world hello', maxsplit=1)
# print(result)
# #
# result = re.split(r'l', 'hello world hello')
# print(result)
# #
# #
# pattern = re.compile('hello')
# result = pattern.findall('hello world hello')
# print(result)
#
# result = re.findall(r'.', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w', "It is a long established fact that a reader")
# print(result)

result = re.findall(r'\w*', "It is a long established fact that a reader")
print(result)

# result = re.findall(r'\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w+$', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'^\w+', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\w\w', "It is a long established fact that a reader")
# print(result)
#
# result = re.findall(r'\b\w', "It is a long established fact that a reader")
# print(result)

result = re.findall(r'@\w+.\w+', "test1@gmail.com, test2@qqq.com, test3@www.com")
print(result)

result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
print(result)

# result = re.findall(r'1\d{1}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-017-2004')
# print(result)
# #
# li = ['9999999999', '999999-999', '99999x9999']

# for val in li:
#     if re.match(r'[0-9]{1}[0-9]{9}', val) and len(val) == 10:
#         print('yes')
#     else:
#         print('no')



