#
# ######################### Homework 4 #############################
#
# # task_4.1
# letter = 0
# digit = 0
# text = input('Enter any text: ')
# for i in text:
#     if i.isalpha():
#         letter += 1
#     elif i.isdigit():
#         digit += 1
# print('Amount of digits =', digit)
# print('Amount of letters =', letter)
#
# # task_4.2
# text = input('Enter your text: ')
# letter = input('Enter your letter to search: ')
# letters = 0
#
# for l in text:
#     if l == letter:
#         letters += 1
# print('Letters found: ', letters)
#
# # task_4.3
# text = input('Enter your text: ')
# find_word = input('Enter word to search: ')
# change_word = input('Enter word you want to change: ')
#
# text = text.replace(find_word, change_word)
# print('Your new text: ', text)
#
# # task_4.4
# sentence = "Hello, world"
# print(sentence[2])
# print(sentence[-2])
# print(sentence[0:5])
# print(sentence[0:-2])
# print(sentence[::2])
# print(sentence[1::2])
# print(sentence[::-1])
# print(sentence[::-2])
#
# print(len(sentence))

####################  additional tasks  #######################

text = input('Input your text: ')

for symbol in range(len(text)):
    if symbol == "." or ". ":
        symbol = (symbol + 1).capitalize()
print(text)




# message = "hello world"
# # [] -> індексатори
# # Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
# # Індекси рахуються з нуля
# print(message[0])
# print(len(message))  # кількість символів у рядку
# # print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

# digit = 0
# count_of_marks = 0
# marks = ".,;:!?()[]{}'\""
#
# for i in text:
#     if i.isdigit():
#         digit += 1
# print('Amount of digits =', digit)
#
# for mark in text:
#     if mark in marks:
#         count_of_marks += 1
# print('Marks found: ', count_of_marks)
#
# exclamation_points = 0
#
# for i in text:
#     if i == "!":
#         exclamation_points += 1
# print('Exclamation points: ', exclamation_points)

#############################################################################################


################################################################
#
# for i in range(5):  # 0, 1, 2, 3, 4
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# for i in range(end, start - 1, -2):
#     # print("Hello")
#     print(i, end=" ")

######
# Показати на екран усі прості числа в діапазоні, вказаному користувачем.
# Число називається простим, якщо воно ділиться без залишку тільки на себе і на одиницю.
# Наприклад, три - це просте число, а чотири - ні.

# start = int(input("Enter start value: "))
# end = int(input("Enter end value: "))
#
# # v1
# if start > end:
#     start, end = end, start

# # v2
# if start > end:
#     temp = start
#     start = end
#     end = temp

###
# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")

############
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()

##############

##
# message = "hello world"
# message_1 = 'hello world'
# print(message)
#
# text = ("hello"
#         "world")
# print(text)
#
# # raw строка
# text = '''
# qwerrty
#     asdfadsvf
#         asdvsvb
# '''
#
# print(text)
#
# # v1
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
# # v2
# path = "C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #
# print("hello, \"world\"\n\tfrom program")

####
#
# dogs, cats = 12, 15
# result = f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}"
# result = result.format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format(dogs, cats)
# print(result)

####
# message = "hello world"
[] -> індексатори
Індекс - це порядковий номер елемента в колекції (масиві). Note: не всі колекції підтримують індекси.
Індекси рахуються з нуля
# print(message[0])
print(len(message))  # кількість символів у рядку
print(message[len(message)])  # IndexError: string index out of range
# print(message[len(message) - 1])
# print(message[-1])

####
###
string - immutable тип даних, рядок змінити не можна
name = "Petya"
# print(name)
name[1] = "r"  # TypeError: 'str' object does not support item assignment
# user_name = "Vasya"
# name = user_name
# print(name)

# # v1
# sentence = "Hello, world"
# for letter in sentence:
#     print(letter, end=" ")
#
# print()
#
# # v2
# for i in range(len(sentence)):
#     print(sentence[i], end=" ")

# slices (срезы)
# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

#
name = "Vasya"
surname = "Petrov"
age = 33
#
fullname = name + " " + surname + " " + str(age)  # конкатенація (додавання рядків)
# print(fullname)

#
# text = "Hello, world" * 3
# print(text)
#
# print("---" * 10)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# print(ord("A"))
# print(chr(98))
######

####
text = "helLo woRlD"

# isalpha(): повертає True, якщо рядок складається лише з алфавітних символів

print(text.isalpha())

# islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі

print(text.islower())

# isupper(): повертає True, якщо всі символи рядка у верхньому регістрі

print(text.isupper())

# isdigit(): повертає True, якщо всі символи рядка - цифри

print(text.isdigit())

# isnumeric(): повертає True, якщо рядок є числом

print(text.isnumeric())

# startswith(str): повертає True, якщо рядок починається з підрядка str

print(text.startswith("helLo"))

# endswith(str): повертає True, якщо рядок закінчується на підрядок str

print(text.endswith("D"))
#
# lower(): перекладає рядок у нижній регістр

print(text.lower())

# upper(): перекладає рядок у верхній регістр

print(text.upper())

# title(): початкові символи всіх слів у рядку перекладаються у верхній регістр

print(text.title())

# capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка
text = "helLo woRlD"

# isalpha(): повертає True, якщо рядок складається лише з алфавітних символів

print(text.isalpha())

# islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі

print(text.islower())

# isupper(): повертає True, якщо всі символи рядка у верхньому регістрі

print(text.isupper())

# isdigit(): повертає True, якщо всі символи рядка - цифри

print(text.isdigit())

# isnumeric(): повертає True, якщо рядок є числом

print(text.isnumeric())

# startswith(str): повертає True, якщо рядок починається з підрядка str

print(text.startswith("helLo"))

# endswith(str): повертає True, якщо рядок закінчується на підрядок str

print(text.endswith("D"))
#
# lower(): перекладає рядок у нижній регістр

print(text.lower())

# upper(): перекладає рядок у верхній регістр

print(text.upper())

# title(): початкові символи всіх слів у рядку перекладаються у верхній регістр

print(text.title())

# capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка

print(text.capitalize())

print(text.capitalize())

# fio = input("Enter fio: ").title()
# print(fio)

#
strip(): видаляє початкові пробіли з рядка
text = "   helLo woRlD   "
print(text)
print(text.lstrip())
#
rstrip(): видаляє кінцеві пробіли з рядка
print(text)
print(text.rstrip())
#
strip(): видаляє початкові та кінцеві пробіли з рядка
print(text)
print(text.strip())
#
ljust(width): якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли,
щоб доповнити значення width, а сам рядок вирівнюється по лівому краю
text = "hello world"
print(text)
print(text.ljust(20))
#
rjust(width): якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли,
щоб доповнити значення width, а сам рядок вирівнюється праворуч
text = "hello world"
print(text)
print(text.rjust(20))
#
center(width): якщо довжина рядка менша за параметр width,
то ліворуч і праворуч від рядка рівномірно додаються пробіли,
щоб доповнити значення width, а сам рядок вирівнюється по центру
text = "hello world"
print(text)
print(text.center(20))

find(str[, start [, end]): повертає індекс підрядка у рядку. Якщо підрядок не знайдено, повертається число -1
text = "hello world"
print(text.find("hello"))  # 0
print(text.find("l"))  # 2
print(text.rfind("l"))  # 9

# first_found_index = text.find("l")
# print(text.find("l", first_found_index + 1))
#
# print(text.find("p"))  # -1
#
# # v1
# text = "hello world"
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)
#
# # v2
# index = 0
# text = "hello world"
#
# for letter in text:
#     if letter == "l":
#         print(index)
#     index += 1

#

replace(old, new[, num]): замінює в рядку один підрядок на інший
text = "hello world hello"
print(text)
#
# # v1
text = text.replace("hello", "goodbye")
# # v2
# text = text.replace("hello", "goodbye", 1)
# print(text)



