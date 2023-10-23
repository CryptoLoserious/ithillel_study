import random

# # # # task_2
# def user_stars(stars):
#     if stars <= 0:
#         return ' '
#     return '*' + user_stars(stars - 1)
#
#
# try:
#     amount_of_stars = int(input('Enter your amount of stars: '))
#     print('This is your stars -> ', user_stars(amount_of_stars))
# except Exception as error:
#     print(error)
#
# """ Запускаємо рекурсію відніманням одиниці від заданого парамерту 'stars'
#     При зменьшенні параметра на одиницю, кожен раз додаємо одиницю і коли параметр буде дорівнювати 0,
#     то функція прийме відповідне значення збільшуючись кожен раз на 1"""

# # user_stars(3) -> user_stars(3 - 1)  => 2 + 1 == 3
# # user_stars(2) -> user_stars(2 - 1)  => 1 + 1
# # user_stars(1) -> user_stars(1 - 1)  => 0 + 1
# # user_stars(0) -> 0


# # # # task_3
# def summa_nums(first, second):
#     if second == 0:
#         return first
#     return summa_nums(first + 1, second - 1)
#
# try:
#     first = int(input('Enter your first number: '))
#     second = int(input('Enter your second number: '))
#     result = summa_nums(first, second)
#     print('Sum your numbers = ', result)
# except Exception as error:
#     print(error)
#
#
# """  Функція збільшує перше задане число на +1, а друге на -1.
#     Коли друге число зменьшиться до 0, а перше на відповідне значення збільшиться, то функція поверне перше число
#     та виведе його як результат складання двох чисел"""
# # #
# # # summa_nums(2, 3) -> summa_nums(3, 2) => 4 + 1 == 5
# # # summa_nums(3, 2) -> summa_nums(4, 1) => 3 + 1
# # # summa_nums(4, 1) -> summa_nums(5, 0) => 2 + 1
# # # summa_nums(5, 0) -> 5

"""_________________________________________________adeed task_______________________________________"""
#
""" for array with 10 numbers"""
#
# def find_min_summa_10nums(numbers):
#     min_summa = numbers[0] + numbers[1]
#     min_start = 0
#
#     for i in range(1, len(numbers) - 1):
#         current_sum = numbers[i] + numbers[i + 1]
#         if current_sum < min_summa:
#             min_summa = current_sum
#             min_start = i
#
#     return numbers[min_start]
#
# NUMS_SIZE = 10
# user_numbers = []
#
# for i in range(NUMS_SIZE):
#     user_numbers.append(random.randint(-10,10))
# print(user_numbers)
# result = find_min_summa_nums(user_numbers)
# print(result)


""" for array with 100 numbers"""
def find_min_summa_100nums(numbers):
    min_summa = sum(numbers[:10])
    min_start = 0

    for i in range(1, len(numbers) - 9):
        current_sum = sum(numbers[i:i + 10])
        if current_sum < min_summa:
            min_summa = current_sum
            min_start = i

    return min_start


NUMS_SIZE = 100
user_numbers = []

for i in range(NUMS_SIZE):
    user_numbers.append(random.randint(-100,100))
print(user_numbers)

result = find_min_summa_100nums(user_numbers)
print(result)
