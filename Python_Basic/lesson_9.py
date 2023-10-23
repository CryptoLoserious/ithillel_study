# import math
# import random
#
#
# def find_min_sum_index(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index + 1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         start_index += 1
#         end_index += 1
#
#         print(f"Min sum: {min_sum} Current sum: {current_sum}")
#
#         return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)
#
#     return min_index
#
#
# nums = [random.randint(1, 10) for _ in range(100)]
# print(nums)
# result = find_min_sum_index(nums, 0, 9)
# print(result)
# # #
# ###########
# import random
#
#
# def generate_random_list(list_len, start_value=1, end_value=100):
#     return [random.randint(start_value, end_value) for _ in range(list_len)]
#
#
# def bubble_sort(nums):
#     swapped = True
#
#     while swapped:
#         swapped = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 swapped = True
#
#
# def selection_sort(nums):
#     for i in range(len(nums)):
#         lowest_value_index = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
#
# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         item_to_insert = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > item_to_insert:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = item_to_insert
#
#
# def merge(left_list, right_list):
#     sorted_list = []
#     left_list_index = right_list_index = 0
#     left_list_length, right_list_length = len(left_list), len(right_list)
#
#     for _ in range(left_list_length + right_list_length):
#         if left_list_index < left_list_length and right_list_index < right_list_length:
#             # порівнюємо перші елементи на початку кожного списку
#             # якщо перший елемент лівого підписку менший - додаємо його
#             if left_list[left_list_index] <= right_list[right_list_index]:
#                 sorted_list.append(left_list[left_list_index])
#                 left_list_index += 1
#             else:
#                 # інакше додамо з правого підписку
#                 sorted_list.append(right_list[right_list_index])
#                 right_list_index += 1
#
#         # якщо досягнуто кінця лівого списку - елементи правого списку додамо до кінця sorted_list
#         elif left_list_index == left_list_length:
#             sorted_list.append(right_list[right_list_index])
#             right_list_index += 1
#         elif right_list_index == right_list_length:
#             sorted_list.append(left_list[left_list_index])
#             left_list_index += 1
#     return sorted_list
#
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     middle_index = len(nums) // 2
#
#     left_list = merge_sort(nums[:middle_index])
#     right_list = merge_sort(nums[middle_index:])
#
#     return merge(left_list, right_list)
#
#
# def partition(nums, low_index, high_index):
#     # вибираємо середній елемент як опорний
#     # так само можливий вибір першого, останнього або довільного ел-тов як опорного
#     pivot = nums[(low_index + high_index) // 2]
#     i = low_index - 1
#     j = high_index + 1
#
#     while True:
#         i += 1
#         while nums[i] < pivot:
#             i += 1
#
#         j -= 1
#         while nums[j] > pivot:
#             j -= 1
#
#         if i >= j:
#             return j
#
#         # Якщо елемент з індексом i (ліворуч від опорного) більше ніж елемент з індексом j (праворуч від опорного) -
#         # то міняємо їх місцями
#         nums[i], nums[j] = nums[j], nums[i]
#
#
# def quick_sort(nums):
#     def _quick_sort(items, low_index, high_index):
#         if low_index < high_index:
#             split_index = partition(items, low_index, high_index)
#             _quick_sort(items, low_index, split_index)
#             _quick_sort(items, split_index + 1, high_index)
#
#     _quick_sort(nums, 0, len(nums) - 1)


# numbers = generate_random_list(5)
# print(numbers)
# # bubble_sort(numbers)
# # selection_sort(numbers)
# # insertion_sort(numbers)
# # numbers = merge_sort(numbers)
# quick_sort(numbers)
# print(numbers)


# def fibonacci(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibonacci(n - 2) + fibonacci(n - 1)
#
#
# for i in range(10):
#     print(fibonacci(i), end=" ")


#################################
# def linear_search_from_start(nums, search_item) -> int:
#     for i in range(len(nums)):
#         if nums[i] == search_item:
#             return i
#     return -1
#
#
# def linear_search_from_end(nums, search_item) -> int:
#     for i in range(len(nums) - 1, -1, -1):
#         if nums[i] == search_item:
#             return i
#     return -1


# numbers = generate_random_list(10, 1, 10)
# print(numbers)
# search_value = 3
# result = linear_search_from_start(numbers, search_value)
# if result != -1:
#     print(f"Value {search_value} found on index: {result}")
# else:
#     print(f"Value {search_value} not found!")
#
# result = linear_search_from_end(numbers, search_value)
# if result != -1:
#     print(f"Value {search_value} found on index: {result}")
# else:
#     print(f"Value {search_value} not found!")

########################
# бінарний пошук працює ТІЛЬКИ на відсортованому масиві
#
# def binary_search(nums, search_item) -> int:
#     first_index = 0
#     last_index = len(nums) - 1
#
#     while first_index <= last_index:
#         middle_index = (first_index + last_index) // 2
#         if nums[middle_index] == search_item:
#             return middle_index
#         else:
#             if search_item < nums[middle_index]:
#                 last_index = middle_index - 1
#             else:
#                 first_index = middle_index + 1
#
#     return -1
#
#
# numbers = sorted(list(set(generate_random_list(10, 1, 5))))
# print(numbers)
# search_value = 3
# result = binary_search(numbers, search_value)
# if result != -1:
#     print(f"Value {search_value} found on index: {result}")
# else:
#     print(f"Value {search_value} not found!")


""" _______________________________________________repeat HW_______________________________________________"""
# #
# def find_min_sum_10nums(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
#     if end_index < len(numbers):
#         current_sum = sum(numbers[start_index:end_index + 1])
#
#         if current_sum < min_sum:
#             min_sum = current_sum
#             min_index = start_index
#
#         start_index += 1
#         end_index += 1
#
#         print(f'Min sum: {min_sum}, Current sum: {current_sum}')
#
#         return find_min_sum_10nums(numbers, start_index, end_index, min_sum, min_index)
#
#     return min_index
#
# nums = [random.randint(1, 100) for _ in range(100)]
# print(nums)
# result = find_min_sum_10nums(nums, 0, 9)
# print(result)




# import re
#
# pattern = r'\+38\((0\w+)|([1-9]\w+)\)\d{7}'
# values = ["+38(099)1234567", "+38(599)1234567","+38(099)", "+38()1234567"]
#
# for val in values:
#     match = re.match(pattern, val)
#     if match:
#         groups = match.groups()
#         if groups[0]:
#             print(f"{val} має 0 після дужки")
#         else:
#             print(f"{val} не має 0 після дужки")

import random
count_source_items = 0
def source_item_index(nums, source_item) -> int:
    global count_source_items
    for i in range(len(nums)):
        if nums[i] == source_item:
            count_source_items += 1
            return i


    return -1

source_item = 7

numbers = [random.randint(1,10) for _ in range(10)]
print(numbers, end=" ")
print(count_source_items)









