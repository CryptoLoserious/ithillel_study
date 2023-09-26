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