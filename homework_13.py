"""Створити ієрархію класів для опису академії.
Зразковий список класів: Person, Teacher, Student, Subject, Academy, і т.д.
Продумати архітектуру: реалізувати принципи ООП
Academy - Building - (Floors - Teachers rooms - Class rooms - bath rooms)  - Person - (Teacher) (Staff) (students)
 Subjects (main subjects - hobbies - sports hobbies) """

class Academy:
    def __init__(self, name, location, accreditation):
        self.__name = name
        self.__accreditation = accreditation
        self.__location = location

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, username):
        if 2 < len(username) < 30:
            self.__name = username

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, set_location):
        for key, value in set_location:
            if 3 <= len(value) <= 30 or value.isnumeric():
                self.__location = set_location
                return
            raise ValueError(f"Invalid value '{key}: {value}")
    def show_info(self):
        print(f"\nName: {self.__name} \nLocation: {self.__location} \nAccreditation: {self.__accreditation}")

class Building(Academy):
    def __init__(self, name, location, floors, class_rooms, bathrooms):
        super().__init__(name, location, None)
        self.__floors = floors
        self.__class_rooms = class_rooms
        self.__bathrooms = bathrooms
    @property
    def floors(self):
        return self.__floors
    @property
    def class_rooms(self):
        return self.__class_rooms
    @property
    def bathrooms(self):
        return self.__bathrooms
    def show_info(self):
        super().show_info()
        print(f"Floors: {self.__floors} \nClass rooms: {self.__class_rooms} \nBathrooms: {self.__bathrooms}")

class Person:
    def __init__(self, name, who_is, age, id_number):
        self.name = name
        self.who_is = who_is
        self.age = age
        self.__id_number = id_number

    def name(self, username):
        if 2 < len(username) < 30:
            self.name = username
        else:
            print("Incorrect name!")

    def who_is(self):
        return self.who_is
    def age(self, age):
        if 17 < age < 150:
            self.age = age
        else:
            print("Incorrect age!")
    @property
    def id_number(self):
        return self.__id_number
    @id_number.setter
    def id_number(self, id_number):
        if 6 <= id_number <= 10:
            self.__id_number = id_number
        else:
            raise Exception("Provide valid id number (from 6 to 10 characters)!")

    def show_info(self):
        print(f"\nPerson name: {self.name} \nIs a: {self.who_is} \nAge: {self.age} \nId_number: {self.__id_number}")

class Teachers(Person):
    __secret_rating_teach = int(0-9)
    def __init__(self, name, who_is, age, id_number, sub_of_teach, teach_exp):
        super().__init__(name, who_is, age, id_number)
        self.sub_of_teach = sub_of_teach
        self.teach_exp = teach_exp

    def sub_of_teach(self):
        return self.sub_of_teach
    def teach_exp(self):
        return self.teach_exp

    def _secret_info(self):
        # __secret_rating_teach = int(input("Enter rating of this teacher: "))
        print(f"Secret code: {self.__secret_rating_teach}")

    def show_info(self):
        super().show_info()
        print(f"Sub_of_teach: {self.sub_of_teach} \nTeach expierence: {self.teach_exp} "
              f"\nSecret rating teacher: {self.__secret_rating_teach}")


class Students(Person):
    def __init__(self, name, who_is, age, id_number, faculty, group_num):
        super().__init__(name, who_is, age, id_number)
        self.faculty = faculty
        self.group_num = group_num

    def faculty(self):
        return self.faculty
    def group_num(self):
        return self.group_num

    def show_info(self):
        super().show_info()
        print(f"Faculty: {self.faculty} \nGroup number: {self.group_num}")


academy = Academy("National Academy", {'country': 'Ukraine', 'city': 'Kyiv', 'street': 'Khreshatik',
                                       'phone_num': '+38(044)1234567'}, "level 4")
academy.show_info()

Main_building = Building("Main building", {'country': 'Ukraine', 'city': 'Kyiv', 'street': 'Khreshatik'},
                    "5", "43", "12")
Main_building.show_info()

vasia = Students("Vasilii", "Student", "23", "2865422", "Geology", 432)
vasia.show_info()
