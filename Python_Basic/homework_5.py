import random
###numbers = [2, -5, 1, 6, 8, -7, 4, 0, 5, -2] - створено для перевірки коду при помилках

#task_5.1:
NUMS_SIZE = 12
numbers = []

for i in range(NUMS_SIZE):
    numbers.append(random.randint(-6,6))
print(numbers)
#
# #task_5.1.1
# sum_neg = 0
# for i in numbers:
#     if i < 0:
#         sum_neg += i
# print('Summa of negative items: ', sum_neg)
#
# # task_5.1.2
# sum_parni = 0
# for j in numbers:
#     if j % 2:
#         sum_parni += j
# print('Summa parni: ', sum_parni)
#
# # task_5.1.3
# sum_neparni = 0
# for p in numbers:
#     if not p % 2:
#         sum_neparni += p
# print('Summa ne parni: ', sum_neparni)
#
# # task_5.1.4
# numbers_3 = numbers[::3]
# product = 1
#
# for num in numbers_3:
#     if num != 0:
#         product *= num
#
# print("Product of elements indices 3:", product)
#
# # task_5.1.5
# numbers_copy = numbers.copy()
# multiply = numbers_copy[numbers.index(min(numbers))] * numbers_copy[numbers.index(max(numbers))]
#
# print('Multiply between min and max: ', multiply)
#
# # task_5.1.6
# # numbers = [2, -5, 1, 6, 8, -7, 4, 0, 5, -2] - як замінник рандому, для перевірки роботи коду

first_pos_index = None
last_pos_index = None

for i in range(len(numbers)):
    if numbers[i] > 0:
        first_pos_index = i
        break

for i in range(len(numbers)-1, -1, -1):
    if numbers[i] > 0:
        last_pos_index = i
        break

sum_middle_num = 0
for i in range(first_pos_index+1, last_pos_index):
        sum_middle_num += numbers[i]

print('Sum of first and last positive nums: ', sum_middle_num)

# # task_5.2:
#
# NUMS_SIZE = 10
# numbers = []
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-5,5))
# print(numbers)
#
# #task_5.2.1
# list_with_pair_nums = []
# for i in numbers:
#     if i % 2 == 0 and i != 0:
#         list_with_pair_nums.append(i)
# print('List with pair nums: ',list_with_pair_nums)
#
# # #task_5.2.2
# list_with_non_pair_nums = []
# for i in numbers:
#     if not i % 2 == 0 and i != 0:
#         list_with_non_pair_nums.append(i)
# print('List with unpair nums: ',list_with_non_pair_nums)
#
# #task_5.2.3
# negative_list = []
#
# for i in numbers:
#     if i < 0:
#         negative_list.append(i)
# print('List with negative num: ', negative_list)
#
# # #task_5.2.4
# positive_list = []
#
# for i in numbers:
#     if i > 0:
#         positive_list.append(i)
# print('List with positive num: ', positive_list)









"""                                       Additional task                                """

# matrix = []
#
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
# print()
#
# # result = 0
# # for i in range(10):
# #     result += matrix[i][i]
# # print(result)
#
# result = 0
# for i in range(10):
#     result += matrix[-i][-i]
# print(result)
