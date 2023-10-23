# ###
# # v2 реалізація інкапсуляції використовуючи анотації властивостей
# class User:
#     __name: str = "no name"  # private поле, доступне тільки всередині цього класу
#     __age: int = 0
#     __secret: int = 12345
#
#     def __init__(self, name=None, age=None):
#         # self.__name = name
#         # self.__age = age
#         # застосуємо інкапсуляцію
#         self.name = name
#         self.age = age
#
#     # getter - для отримання значення приватного поля
#     @property
#     def name(self):
#         return self.__name
#
#     # setter - для санкціонованого доступу до приватної змінної (поля)
#     @name.setter
#     def name(self, name):
#         if 2 < len(name) < 50:
#             self.__name = name
#         else:
#             print("Incorrect name length!")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 18 < age < 150:
#             self.__age = age
#         else:
#             print("Incorrect age!")
#
#     # public method - публічна (доступна зовні) функція
#     def show_info(self):
#         print(f"Name: {self.__name} age: {self.__age}")
#         # self.__secret_info()
#
#     # private method - приватна (недоступна зовні) функція
#     def __secret_info(self):
#         print(f"Secret code: {self.__secret}")
#
#
# anton = User("Anton", -34)
# anton.show_info()
# anton.age = 40
# anton.show_info()
# anton.age = 400
# anton.show_info()
# print(anton.name)

####################
# class MyConverter:
#     __money_sum = 0
#     __uah_rate = 37.4
#     __converter_direction = 1
#
#     def __init__(self, input_money, convert_dir):
#         self.money_sum = input_money
#         self.converter_direction = convert_dir
#
#     @property
#     def converter_direction(self):
#         return self.__converter_direction
#
#     @converter_direction.setter
#     def converter_direction(self, convert_dir):
#         if convert_dir == 1 or convert_dir == 2:
#             self.__converter_direction = convert_dir
#         else:
#             raise Exception("Provide correct converter direction!")
#
#     @property
#     def money_sum(self):
#         return self.__money_sum
#
    # @money_sum.setter
    # def money_sum(self, input_sum):
    #     if 0 < input_sum < 1000000000:
    #         self.__money_sum = input_sum
    #     else:
    #         raise Exception("Provide valid money sum!")
#
#     # readonly property
#     @property
#     def uah_rate(self):
#         return self.__uah_rate
#
#     def show_uah_rate(self):
#         print(f"Current UAH rate: {self.__uah_rate}")
#
#     def show_result(self):
#         print(self.__getMoneyResult())
#
#     def __getMoneyResult(self):
#         match self.__converter_direction:
#             case 1:
#                 return f"{self.__money_sum} UAH = {self.__get_usd_sum()} USD"
#             case 2:
#                 return f"{self.__money_sum} USD = {self.__get_uah_sum()} UAH"
#             case _:
#                 raise Exception("Incorrect converter direction!")
#
#     def __get_usd_sum(self):
#         return self.__money_sum / self.__uah_rate
#
#     def __get_uah_sum(self):
#         return self.__money_sum * self.__uah_rate
#
#
# try:
#     converter = MyConverter(5000, convert_dir=1)
#     converter.show_result()
# except Exception as error:
#     print(error)

######################
class Person:
    __name = "no name"
    __age = 18

    def __init__(self, name, age, hobby="no hobby"):
        self.name = name
        self.age = age
        self.hobby = hobby

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, username):
        if 2 < len(username) < 30:
            self.__name = username

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, user_age):
        if 18 <= user_age < 150:
            self.__age = user_age

    def show_info(self):
        print(f"Name: {self.__name} age: {self.__age}")


class Company:
    __name = "demo name"

    def __init__(self, company_name: str, users: list = None):
        self.__name = company_name
        self.users: list[Person] = users

    def show_users(self):
        print(f"Found {len(self.users)} users")
        for user in self.users:
            user.show_info()

    def add_user(self, new_user: Person):
        if isinstance(new_user, Person):
            self.users.append(new_user)
            return
        raise Exception(f"Provided value with incorrect type: {type(new_user)}!")


try:
    users: list = [Person("Vasya", 33), Person("Petya", 44), Person("Anton", 55)]
    google = Company("Google", users)
    google.show_users()
    google.add_user(Person("Anton111", 66))
    google.show_users()
    google.add_user("test")
except Exception as error:
    print(error)

###################################
# успадкування
# v1
# class Person:
#     __name = "noname"
#     __age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 12345  # (private) -> доступ тільки всередині класу
#         self._hobby = "no info"  # (protected) -> доступ усередині класу та в класах спадкоємців
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 18:
#             self.__age = age
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Employee(Person):  # успадковуємося від класу Person
#     def work(self):
#         print(f"{self.name} works!")
#         # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#         print(self._hobby)  # є доступ так як у базовому класі це поле protected
# #
# #
# vasya = Employee("Vasya", 33)
# vasya.show_info()
# vasya.work()
# #
# # print(vasya._hobby)  # до protected полів не варто звертатися безпосередньо, краще використовувати геттер
# print(vasya.hobby)


##
# v2
# class Person:
#     __name = "noname"
#     __age = 18
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__secret = 12345  # (private) -> доступ тільки всередині класу
#         self._hobby = "no info"  # (protected) -> доступ усередині класу та в класах спадкоємців
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if len(name) > 2:
#             self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 18:
#             self.__age = age
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# class Employee(Person):  # успадковуємося від класу Person
#     def __init__(self, name, age, company):
#         # v1
#         super().__init__(name, age)  # виклик конструктора базового класу Person
#         # super() -> посилання на базовий клас, отримуємо доступ до елементів базового класу
#         # v2
#         # Person.__init__(self, name, age)
#         self.company = company
#
#     # def work(self):
#     #     print(f"{self.name} works in {self.company} company")
#     #     # print(self.__secret)  # AttributeError: 'Employee' object has no attribute '_Employee__secret'
#     #     print(self._hobby)  # є доступ так як у базовому класі це поле protected
#     #     # print(super().show_info())
#     #     # print(super().name)
#
#     # перевизначення методу
#     def show_info(self):
#         super().show_info()  # виклик методу базового класу
#         print(f"Works in {self.company} company")  # розширили своєю логікою
#
#
# vasya = Employee("Vasya", 33, "Google")
# vasya.show_info()
# # vasya.work()

#####################
###
# v3
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def work(self):
#         print(f"{self.name} works!")
#
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name} studies!")
#
#
# class WorkingStudent(Student, Employee):  # множинне спадкування
#     pass
#
#
# vasya = WorkingStudent("Vasya")
# vasya.work()
# vasya.study()
# print(WorkingStudent.mro())
# [<class '__main__.WorkingStudent'>, <class '__main__.Student'>, <class '__main__.Employee'>, <class 'object'>]

# v4 приклад ромбоподібного наслідування
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}\nAge: {self.age}")
#
#
# class Employee(Person):
#     def __init__(self, name, age, company=None):
#         super().__init__(name, age)
#         self.company = company
#
#     def show_info(self):
#         super().show_info()
#         print(f"Company: {self.company}")
#
#
# class Student(Person):
#     def __init__(self, name, age, university=None):
#         super().__init__(name, age)
#         self.university = university
#
#     def show_info(self):
#         super().show_info()
#         print(f"University: {self.university}")
#
#
# class WorkingStudent(Student, Employee):
#     def __init__(self, name, age, company, university):
#         Student.__init__(self, name, age, university)
#         Employee.__init__(self, name, age, company)
#
#     def show_info(self):
#         super().show_info()
#         # Student.show_info(self)
#         # Employee.show_info(self)
#
#
# vasya = WorkingStudent("Vasya", 33, "Google", "Tech")
# vasya.show_info()
# # print(vasya.company)
# # print(vasya.university)
# print(WorkingStudent.mro())

##
# https://makina-corpus.com/python/python-tutorial-understanding-python-mro-class-search-path
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

####
# додати інкапсуляцію
# class Transport:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def show_info(self):
#         print(f"Name: {self.name}\nyear: {self.year}")
#
#
# class BaseAuto(Transport):
#     def __init__(self, name, year, wheels_count=0):
#         super().__init__(name, year)
#         self.wheels_count = wheels_count
#
#     # перекриття методу базового класу Transport
#     def show_info(self):
#         print(f"Wheels count: {self.wheels_count}")
#
#
# class WaterTransport(Transport):
#     def __init__(self, name, year, displacement=0.):
#         super().__init__(name, year)
#         self.displacement = displacement
#
#     # перекриття методу базового класу Transport
#     def show_info(self):
#         print(f"Displacement: {self.displacement}")
#
#
# class Auto(BaseAuto):
#     def __init__(self, name, year, wheels_count, machine_body_form_factor):
#         super().__init__(name, year, wheels_count)
#         self.machine_body_form_factor = machine_body_form_factor
#
#     # перекриття методу базового класу BaseAuto
#     def show_info(self):
#         print(f"Machine body form factor: {self.machine_body_form_factor}")
#
#
# class Amphibian(WaterTransport, BaseAuto):
#     def __init__(self, name, year, wheels_count, displacement):
#         WaterTransport.__init__(self, name, year, displacement)
#         BaseAuto.__init__(self, name, year, wheels_count)
#
#     # перевизначення методу show_info
#     def show_info(self):
#         Transport.show_info(self)
#         WaterTransport.show_info(self)
#         BaseAuto.show_info(self)
#
#
# test_car = Amphibian("BMW", 2023, 4, 123.2)
# test_car.show_info()
# print(Amphibian.mro())

####################
# поліморфізм
# https://maxdrive.kyiv.ua/dokumentacija/pochta/chto-takoe-polimorfizm-v-python

# len([])
# len({})
# len("")
#
#
# class Parrot:
#     __name = "Kesha"
#
#     def fly(self):
#         print(f"Parrot {self.__name} can fly")
#
#     def swim(self):
#         print(f"Parrot {self.__name} can't swim")
#
#
# class Penguin:
#     __name = "Bobik"
#
#     def fly(self):
#         print(f"Penguin {self.__name} can't fly")
#
#     def swim(self):
#         print(f"Penguin {self.__name} can swim")
#
#
# # загальний інтерфейс
# def show_animal_info(bird):
#     # на цьому етапі нам все одно якого типу буде екземпляр – інтерфейс взаємодії однаковий: fly and swim
#     bird.fly()
#     bird.swim()
#
#
# # створюємо об'єкти
# my_parrot = Parrot()
# my_penguin = Penguin()
#
# # передамо в загальний інтерфейс екземпляри
# show_animal_info(my_parrot)
# show_animal_info(my_penguin)

####################
# class InvoiceType:
#     classic = "Classic invoice"
#     urgent = "Urgent invoice"
#
#     @staticmethod
#     def show_all_types():
#         print(InvoiceType.classic)
#         print(InvoiceType.urgent)
#
#
# print(InvoiceType.urgent)
# InvoiceType.show_all_types()

#########################

