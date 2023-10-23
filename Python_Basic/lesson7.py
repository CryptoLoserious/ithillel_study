# 3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.
# Визначте, скільки різних слів міститься у цьому тексті.


# line_number = input("Enter line number: ")
# text = ""
#
# for i in range(int(line_number)):
#     text += input(f"Enter {i + 1} text line: ") + " "
#
# print(text)
#
# text = " ".join(list(set(text.split())))
# print(text)

# # Є список цілих, заповнений випадковими числами.
# import random
#
# numbers1 = []
#
# for _ in range(10):
#     numbers1.append(random.randint(-10, 10))
#
# print(numbers1)
#
# # На підставі даних цього масиву потрібно:
# #
# # ■ Створити список цілих, що містить лише парні числа з першого списку;
# numbers2 = []
#
# for number in numbers1:
#     if number % 2 == 0:
#         numbers2.append(number)
#
# print(numbers2)
# # ■ Створити список цілих, що містить лише непарні числа з першого списку;
# numbers2 = []
# for number in numbers1:
#     if number % 2 != 0:
#         numbers2.append(number)
#
# print(numbers2)
# # ■ Створити список цілих, що містить лише негативні числа з першого списку;
# numbers2 = []
# for number in numbers1:
#     if number < 0:
#         numbers2.append(number)
#
# print(numbers2)
# # ■ Створити список цілих, що містить лише позитивні числа з першого списку.
# numbers2 = []
# for number in numbers1:
#     if number >= 0:
#         numbers2.append(number)
#
# print(numbers2)
###################

# У списку цілих, заповненому випадковими числами обчислити:
# import random
#
# numbers = []
#
# for _ in range(10):
#     numbers.append(random.randint(-10, 10))
#
# print(numbers)
#
# ■ Добуток елементів з кратними індексами 3;
# result = 0
#
# for i in range(len(numbers)):
#     if i % 3 == 0 and i != 0:
#         print(i, end=" ")
#         result += numbers[i]
#
# print(f"\n{result}")

# ■ Добуток елементів між мінімальним та максимальним елементом;
# result = 0
# min_value = min(numbers)
# max_value = max(numbers)
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
# print(min_value)
# print(max_value)
# print(min_value_index)
# print(max_value_index)
#
# if min_value_index > max_value_index:
#     min_value_index, max_value_index = max_value_index, min_value_index
#
# for i in range(min_value_index + 1, max_value_index):
#     result += numbers[i]
#
# print(f"\n{result}")

# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.
# result = 0
#
# first_positive_index = 0
# last_positive_index = 0
#
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         first_positive_index = i
#         break
#
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] > 0:
#         last_positive_index = i
#         break
#
# print(first_positive_index)
# print(last_positive_index)
#
# for i in range(first_positive_index + 1, last_positive_index):
#     result += numbers[i]
#
# print(f"\n{result}")

###############
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
#
# вивести на екран

# import random
#
# matrix = []
# matrix_size = 5
#
# for i in range(matrix_size):
#     matrix.append([])
#     for j in range(matrix_size):
#         matrix[i].append(random.randint(10, 99))
#
# for i in range(matrix_size):
#     for j in range(matrix_size):
#         print(matrix[i][j], end=" ")
#     print()
#
# #
# # - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# # (аналогічно зробити з рядком)
# column_number_1 = int(input("Enter first column number: "))
#
# if column_number_1 < 1 or column_number_1 > matrix_size:
#     print("Incorrect column!")
# else:
#     column_number_2 = int(input("Enter second column number: "))
#
#     if column_number_2 < 1 or column_number_2 > matrix_size:
#         print("Incorrect column!")
#     else:
#         for i in range(matrix_size):
#             matrix[i][column_number_1 - 1], matrix[i][column_number_2 - 1] =\
#                 matrix[i][column_number_2 - 1], matrix[i][column_number_1 - 1]
#
# for i in range(matrix_size):
#     for j in range(matrix_size):
#         print(matrix[i][j], end=" ")
#     print()

################
def say_hello():
    print("Hello")


try:
    number = 10
    print(number)
    print(say_hello)
    say_hello()  # виклик функції (функція починає працювати)
#     say_hello()
# except Exception as error:
#     print(error)
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()


# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)

####################
# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
#

# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)

########
# def add(n1, n2):
#     return n1 + n2
#
#
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
#
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів

# def add(n1, n2):
#     return n1 + n2
#
#
# def sub(n1, n2):
#     return n1 - n2
#
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             print(f"{first_number} {math_operation} {second_number} = {add(first_number, second_number)}")
#         case "-":
#             print(f"{first_number} {math_operation} {second_number} = {sub(first_number, second_number)}")
#         case "*":
#             print(f"{first_number} {math_operation} {second_number} = {mult(first_number, second_number)}")
#         case "/":
#             print(f"{first_number} {math_operation} {second_number} = {division(first_number, second_number)}")
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     calculate()
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)


###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# user_info("Vasya", 33, "test")
# user_info("Vasya", 33)
# user_info("Vasya")
#
# user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)
#
# my_hobby = "walking"
# user_info(hobby=my_hobby, name="Petya", age=33)

##############
# Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(name="Bob", age=41, company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)
#
#
# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

########
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# def get_list_sum(numbers):
#     numbers_sum = 0
#
#     for num in numbers:
#         numbers_sum += num
#
#     return numbers_sum
#
#
# my_numbers = [n for n in range(3)]
# print(my_numbers)
# result = get_list_sum(my_numbers)
# print(result)

############
# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.

# import random
#
#
# def create_list_with_random_values(list_length=10, start_value=1, end_value=10) -> list:
#     new_list = []
#
#     for _ in range(list_length):
#         new_list.append(random.randint(start_value, end_value))
#
#     return new_list
#
#
# def remove_duplicates(numbers) -> list:
#     return list(set(numbers))
#
#
# def get_unique_values(numbers: list) -> None:
#     for number in numbers:
#         if numbers.count(number) == 1:
#             print(number)
#
#
# my_numbers = create_list_with_random_values()
# print(my_numbers)
# my_numbers_without_duplicates = remove_duplicates(my_numbers)
# print(my_numbers_without_duplicates)
# get_unique_values(my_numbers)

##############
# Дано два списки чисел.
#
# Порахуйте, скільки чисел міститься як у першому списку, так і у другому.

# def calc_number_of_equals_numbers(number_1: list, number_2: list) -> int:
#     print(set(number_1).intersection(set(number_2)))
#     return len(set(number_1).intersection(set(number_2)))
#
#
# nums1 = [1, 3, 5, 2]
# nums2 = [1, 6, 2, 9]
# print(calc_number_of_equals_numbers(nums1, nums2))
