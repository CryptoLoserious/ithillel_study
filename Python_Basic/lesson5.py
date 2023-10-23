# text = "hello world. goodbye world."
#
# search_item = ". "
# current_index = text.find(search_item)
# print(current_index)
#
# first_sentence = text[:current_index + len(search_item)]
# print(first_sentence)
#
# second_sentence = text[current_index + len(search_item):]
# print(second_sentence)
#
# final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
# print(final_sentence)


# numbers = []
# numbers1 = list()
# print(type(numbers))
# print(type(numbers1))

# numbers = [1, 4, 5, 1, 5]
#
# print(numbers)
# print(numbers[0])
#
# numbers[1] = 1111
# print(len(numbers))
# print(numbers[-1])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(numbers, end=" ")
#
# print()
# import random
#
# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1,10))
# print(numbers)


# people = ['Tom', 'Bill', 'alice', 'Tomas', 'jully']
# numbers. reverse()


# Є певний текст. Реалізуйте наступну функціональність:
#
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;

# text = "hello world. goodbye world."
#
# search_item = ". "
# current_index = text.find(search_item)
# print(current_index)
#
# first_sentence = text[:current_index + len(search_item)]
# print(first_sentence)
#
# second_sentence = text[current_index + len(search_item):]
# print(second_sentence)
#
# final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
# print(final_sentence)
#
# ####
# print(final_sentence.count("l"))

####
# list
# numbers = []
# numbers_1 = list()
# print(type(numbers))
# print(type(numbers_1))

# numbers = [1, 3, 25, 7, 2, 7]

# print(numbers)
# print(numbers[0])
#
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()

# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3]
# print(nums)
# result = []
# for i in nums:
#     result.append(i* 5)
# print(result)

#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])

# Розкладання списку (декомпозиція)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

####
#
# import random
#
# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
# #
# print(numbers)
# # # append(item): додає елемент item до кінця списку
# #
# numbers.append(2222)
# print(numbers)
# #
# # # insert(index, item): додає елемент item до списку за індексом index
# #
# numbers.insert(1, 3333)
# print(numbers)
# #
# # # extend(items): додає набір елементів items до кінця списку
# #
# numbers.extend([2, 3, 4])
# print(numbers)
# #
# numbers += [1, 2, 3, 4]  # numbers = numbers + [1, 2, 3, 4]
# print(numbers)
# #
# # # remove(item):видаляє елемент item. Видаляється лише перше входження елемента.
# # # Якщо елемент не знайдено, генерує виняток ValueError
# #
# numbers.remove(2222)
# print(numbers)
#
# # clear(): видалення всіх елементів зі списку
#
# numbers.clear()
# print(numbers)
#
# del numbers
# print(numbers)
#
# # index(item): повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
#
# print(numbers.index(2))
#
# # pop([index]): видаляє та повертає елемент за індексом index.
# # Якщо індекс не передано, просто видаляє останній елемент.
#
# result = numbers.pop(0)
# print(result)
# print(numbers)
# #
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): повертає кількість входжень елемента item до списку
# #
# print(numbers.count(3))

sort([key]): Сортує елементи. За умовчанням сортує за зростанням.
Але за допомогою key ми можемо передати функцію сортування.
sorted(list, [key]): повертає відсортований список

v1
numbers.sort()
print(numbers)
v2
numbers_sorted = sorted(numbers)
print(numbers_sorted)
print(numbers)

people = ["Tom", "bob", "alice", "Sam", "Bill"]
v1
people.sort()
print(people)
v2
people.sort(key=str.lower)
print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# # reverse(): розставляє всі елементи у списку у зворотному порядку
#
# numbers.reverse()
# print(numbers)
#
# # copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Крім того, Python надає ряд вбудованих функцій для роботи зі списками:
# #
# # len(list): повертає довжину списку
#
# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
# #
# letters = ["ab", "ac"]
# print(max(letters))

###############
# text = "hello world. goodbye world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentence = search_item.join(result)
# print(result_sentence)

##
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]

# numbers = [3, 1, 4, 2, 5]
# numbers_copy = numbers.copy()
#
# print(numbers)
#
# numbers_copy[numbers.index(min(numbers))], numbers_copy[numbers.index(max(numbers))] = max(numbers), min(numbers)
# numbers = numbers_copy.copy()
#
# print(numbers)

# min_value = min(numbers)
# max_value = max(numbers)
#
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# numbers[min_value_index] = max_value
# numbers[max_value_index] = min_value
#
# print(numbers)

# problem
# numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))] = 111, 222
# numbers[numbers.index(min(numbers))] = 111
# numbers[numbers.index(max(numbers))] = 222

# print(numbers)

###############
# numbers = ["Vasya", 33, ["dance", "walk"]]
# print(numbers)
# print(numbers[2])
# print(numbers[2][0])

##
# v1
# array = [
#     [1, 3, 2],
#     [1, 4],
#     1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
# print(array[3][1][1])
# v2
# matrix = [
#     [24, 41, 15, 62],
#     [22, 41, 15, 62],
#     [25, 42, 11, 66],
#     [27, 46, 16, 63]
# ]
#
# print(matrix[0][1])
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#
# import random
#
# matrix = []

# print(matrix)
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
#
# # v1
# # print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#############
###
# import random
#
# words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]
#
# secret_word = words[random.randint(0, len(words) - 1)]
# # print(secret_word)
#
# user_word = ["_"] * len(secret_word)
# print(user_word)
# print(" ".join(user_word))

# attempts_counter = 0
#
# while True:
    # v1
    # if "".join(user_word).find("_") == -1:
    #     print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
    #     break

    # v2
    # if "".join(user_word).lower() == secret_word.lower():
    #     print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
    #     break
    #
    # print(" ".join(user_word))
    #
    # letter = input("Enter letter: ").strip().lower()
    # attempts_counter += 1
    #
    # if not letter.isalpha() or len(letter) != 1:
    #     print("Please enter only one letter!")
    #     continue
    #     # или
    #     # raise Exception("Please enter only one letter!")
    #
    # for i in range(len(secret_word)):
    #     if letter == secret_word[i].lower():
    #         user_word[i] = letter

# добавить ограничение на кол-во попыток, если не уложились в кол-во - проиграли




# """         """"""""""""""""""""""""""      HOMEWORK           """""""""""""""""""""""""       """




# Є певний текст. Реалізуйте наступну функціональність:
#
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;

# text = "hello world. goodbye world."
#
# search_item = ". "
# current_index = text.find(search_item)
# print(current_index)
#
# first_sentence = text[:current_index + len(search_item)]
# print(first_sentence)
#
# second_sentence = text[current_index + len(search_item):]
# print(second_sentence)
#
# final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
# print(final_sentence)
#
# ####
# print(final_sentence.count("l"))

####
# list
# numbers = []
# numbers_1 = list()
# print(type(numbers))
# print(type(numbers_1))

# numbers = [1, 3, 25, 7, 2, 7]

# print(numbers)
# print(numbers[0])
#
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()

# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])

# Розкладання списку (декомпозиція)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

####
#
# import random
#
# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
# #
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(1, 10))
# #
# print(numbers)
# # # append(item): додає елемент item до кінця списку
# #
# numbers.append(2222)
# print(numbers)
# #
# # # insert(index, item): додає елемент item до списку за індексом index
# #
# numbers.insert(1, 3333)
# print(numbers)
# #
# # # extend(items): додає набір елементів items до кінця списку
# #
# numbers.extend([2, 3, 4])
# print(numbers)
# #
# numbers += [1, 2, 3, 4]  # numbers = numbers + [1, 2, 3, 4]
# print(numbers)
# #
# # # remove(item):видаляє елемент item. Видаляється лише перше входження елемента.
# # # Якщо елемент не знайдено, генерує виняток ValueError
# #
# numbers.remove(2222)
# print(numbers)
#
# # clear(): видалення всіх елементів зі списку
#
# numbers.clear()
# print(numbers)
#
# del numbers
# print(numbers)
#
# # index(item): повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
#
# print(numbers.index(2))
#
# # pop([index]): видаляє та повертає елемент за індексом index.
# # Якщо індекс не передано, просто видаляє останній елемент.
#
# result = numbers.pop(0)
# print(result)
# print(numbers)
# #
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): повертає кількість входжень елемента item до списку
# #
# print(numbers.count(3))

# sort([key]): Сортує елементи. За умовчанням сортує за зростанням.
# Але за допомогою key ми можемо передати функцію сортування.
# sorted(list, [key]): повертає відсортований список

# v1
# numbers.sort()
# print(numbers)
# v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# v1
# people.sort()
# print(people)
# v2
# people.sort(key=str.lower)
# print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# # reverse(): розставляє всі елементи у списку у зворотному порядку
#
# numbers.reverse()
# print(numbers)
#
# # copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Крім того, Python надає ряд вбудованих функцій для роботи зі списками:
# #
# # len(list): повертає довжину списку
#
# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
# #
# letters = ["ab", "ac"]
# print(max(letters))

###############
# text = "hello world. goodbye world."
# search_item = ". "
#
# sentences = text.split(search_item)
# print(sentences)
#
# result = []
#
# for sentence in sentences:
#     result.append(sentence.capitalize())
#
# print(result)
#
# result_sentence = search_item.join(result)
# print(result_sentence)

##
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]

# numbers = [3, 1, 4, 2, 5]
# numbers_copy = numbers.copy()
#
# print(numbers)
#
# numbers_copy[numbers.index(min(numbers))], numbers_copy[numbers.index(max(numbers))] = max(numbers), min(numbers)
# numbers = numbers_copy.copy()
#
# print(numbers)

# min_value = min(numbers)
# max_value = max(numbers)
#
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# numbers[min_value_index] = max_value
# numbers[max_value_index] = min_value
#
# print(numbers)

# problem
# numbers[numbers.index(min(numbers))], numbers[numbers.index(max(numbers))] = 111, 222
# numbers[numbers.index(min(numbers))] = 111
# numbers[numbers.index(max(numbers))] = 222

# print(numbers)

###############
# numbers = ["Vasya", 33, ["dance", "walk"]]
# print(numbers)
# print(numbers[2])
# print(numbers[2][0])

##
# v1
# array = [
#     [1, 3, 2],
#     [1, 4],
#     1,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
# print(array[3][1][1])
# v2
# matrix = [
#     [24, 41, 15, 62],
#     [22, 41, 15, 62],
#     [25, 42, 11, 66],
#     [27, 46, 16, 63]
# ]
#
# print(matrix[0][1])
#
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#
# import random
#
# matrix = []

# print(matrix)
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
#
# # v1
# # print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

#############
###
# import random
#
# words = ["Cat", "Apple", "Dog", "Letter", "Helicopter"]
#
# secret_word = words[random.randint(0, len(words) - 1)]
# # print(secret_word)
#
# user_word = ["_"] * len(secret_word)
# # print(user_word)
# # print(" ".join(user_word))
#
# attempts_counter = 0
#
# while True:
    # v1
    # if "".join(user_word).find("_") == -1:
    #     print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
    #     break

    # v2
    # if "".join(user_word).lower() == secret_word.lower():
    #     print(f"\nYou guessed a word!\nWord: {secret_word}\nAttempts: {attempts_counter}")
    #     break
    #
    # print(" ".join(user_word))
    #
    # letter = input("Enter letter: ").strip().lower()
    # attempts_counter += 1
    #
    # if not letter.isalpha() or len(letter) != 1:
    #     print("Please enter only one letter!")
    #     continue
    #     # или
    #     # raise Exception("Please enter only one letter!")
    #
    # for i in range(len(secret_word)):
    #     if letter == secret_word[i].lower():
    #         user_word[i] = letter

# добавить ограничение на кол-во попыток, если не уложились в кол-во - проиграли








