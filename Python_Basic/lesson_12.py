# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.
#
# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.
#
# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.
#
# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації
#
# ###
# # self - посилання на контекст класу, екземпляр класу
# # контекст класу - все що є частиною класу (экземпляра)
# __init__ Конструктор класу – дозволяє створити екземпляр класу. Можливо з параметрами та без параметрів.
#
# статичний метод (функція), поле (змінна) відносяться до класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів та інших службових об'єктів, там де немає сенсу
# створювати екземпляри
class Car:
    # def __new__(cls, *args, **kwargs):
    #     pass
    #
    # def __init__(self):
    #     pass

    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def show_details(self):
        print(f"Name: {self.name} Color: {self.color} Price: {self.price}")

    @staticmethod
    def show_info():
        print("This is car")
#
#
# toyota = Car("toyota", 123456, "green")
# toyota.show_info()
# toyota.show_details()
# # print(toyota.price)
# # print(toyota.color)
# # Car.show_details(toyota)
# Car.show_info()
#
# car_price = 22326752367
# car_color = "red"
# bmw = Car("bmw", car_price, car_color)
# bmw.show_info()
# bmw.show_details()
#
# # print(bmw.price)
# # print(bmw.color)
# # print(type(bmw))
# # print(bmw.name)

##################
# інкапсуляція
# v1
# class User:
#     __name: str = "no name"  # private поле, доступне тільки всередині цього класу
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name=None, age=None):
#         # self.__name = name
#         # self.__age = age
#         # застосуємо інкапсуляцію
#         self.set_age(age)
#         self.set_name(name)
#
#     def set_name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     def get_age(self):
#         return self.__age
#
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         # self.__secret_info()
#
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
#
#
# vasya = User("Vasya", -44)
# vasya.show_info()
# vasya.set_age(100)
# vasya.show_info()
# vasya.set_age(-100)
# vasya.show_info()

# vasya.__secret_info()
# vasya._User__secret_info()  # так робити не треба так як це ламає інкапсуляцію
