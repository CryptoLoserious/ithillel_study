# # # task 1:
# def summa(numbers: list) -> int:
#     my_mult = 1
#     for i in numbers:
#         my_mult *= i
#     return my_mult
#
# my_numbers = [j for j in range(2, 9)]
# print(my_numbers)
# result = summa(my_numbers)
# print('Sum of all items in the list: ', result)

# # task 2:
# v1:
# def minimum(numbers: list) -> int:
#     return min([i for i in numbers])

# # v2:
# def minimum(numbers: list) -> int:
#     min_number = numbers[0]
#     for i in numbers:
#         if i < min_number:
#             min_number = i
#     return min_number
#
# my_numbers = [j for j in range(4, 17)]
# print(my_numbers)
# result = minimum(my_numbers)
# print('The minimum value in the list: ', result)

# # # task3









#
# # task4
# def deliete(numbers: list) -> int:
#     while True:
#         try:
#             my_num_for_del = int(input('Input number for remove: '))
#         except ValueError:
#             print('Enter ONLY integer items!')
#             continue
#         count_of_items = 0
#         while my_num_for_del in numbers:
#             numbers.remove(my_num_for_del)
#             count_of_items += 1
#         return count_of_items
#
# my_numbers = [2, 8, 5, 6, 10, 11, 4, 8, 8, 9, 0, 11, 8]
# print(my_numbers)
# try:
#     result = deliete(my_numbers)
#     print('Remove items from the list: ', result)
# except Exception as error:
#     print(error)

# #task5:
# def add_list(numbers1: list, numbers2: list) -> int:
#     new_list = []
#     for i in numbers2:
#         if i in numbers1:
#             new_list.append(i)
#     return new_list
#
# numbers1 = [j for j in range(1, 11)]
# print('The first list: ', numbers1)
# numbers2 = [p for p in range(3, 15)]
# print('The second list: ', numbers2)
# result = add_list(numbers1, numbers2)
# print('Identical items from lists: ', result)

# # # task6:
# def degree_of_num(numbers: list) -> int:
#     while True:
#         try:
#             num_of_degree = int(input('Enter your number of degree: '))
#         except ValueError:
#             print('Enter ONLY integer items!')
#             continue
#         degree_list = []
#         for i in numbers:
#             degree_list.append(i ** num_of_degree)
#         return degree_list
#
# my_numbers = [j for j in range(1, 11)]
# print(my_numbers)
# try:
#     result = degree_of_num(my_numbers)
#     print('After entering the degree, the values in the list are equal to: ','\n',result)
# except Exception as error:
#     print(error)


