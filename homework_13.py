"""Створити ієрархію класів для опису академії.
Зразковий список класів: Person, Teacher, Student, Subject, Academy, і т.д.
Продумати архітектуру: реалізувати принципи ООП
Academy - Building - (Floors - Teachers rooms - Class rooms - bath rooms)  - Person - (Teacher) (Staff) (students)
 Subjects (main subjects - hobbies - sports hobbies) """

class Academy:
    __name = None
    __accreditation = None
    __location = {
        'country': None,
        'city': None,
        'street': None,
        'phone_num': None,
    }
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
        print(f"Name: {self.__name} \nLocation: {self.__location} \nAccreditation: {self.__accreditation}")

class Building(Academy):
    __floors = None
    __class_rooms = None
    __bathrooms = None
    def __init__(self, name, location, floors, class_rooms, bathrooms):
        super().__init__(name, location)
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
        print(f"Name: {self.__name} \nLocation: {self.__location} \nfloors: {self.__floors} \nclass_rooms: {self.__class_rooms}"
              f"\nbathrooms: {self.__bathrooms}")

class Person(Academy):
    age = None
    __id_number = None
    def __init__(self, name, age, id_number):
        super().__init__(name)
        self.__age = age
        self.__id_number = id_number
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if 17 < age < 150:
            self.__age = age
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
        print(f"Name: {self.__name} \nage: {self.__age} \nid_number: {self.__id_number}")

class Teachers(Person):
    # sub_of_teach = None
    # teach_exp = None
    __secret_rating_teach = int(0-9)
    def __init__(self, name, age, id_number, sub_of_teach, teach_exp):
        super().__init__(name, age, id_number)
        self.sub_of_teach = sub_of_teach
        self.teach_exp = teach_exp

    def sub_of_teach(self):
        return self.sub_of_teach
    def teach_exp(self):
        return self.teach_exp

    def __secret_info(self):
        print(f"Secret code: {self.__secret_rating_teach}")

    def show_info(self):
        print(f"Name: {self.__name} \nage: {self.__age} \nid_number: {self.__id_number} \nsub_of_teach: {self.sub_of_teach}"
              f"\nteach_exp: {self.teach_exp}")

class Students(Person):
    __secret_rating_learn = int(0 - 9)
    def __init__(self, name, age, id_number, faculty, group_num):
        super().__init__(name, age, id_number)
        self.faculty = faculty
        self.group_num = group_num

    def faculty(self):
        return self.faculty
    def group_num(self):
        return self.group_num

    def show_info(self):
        print(f"Name: {self.__name} \nLocation: {self.__location} \nAccreditation: {self.__accreditation}")


academy = Academy("National Academy", {'country': 'Ukraine', 'city': 'Kyiv', 'street': 'Khreshatik',
                                       'phone_num': '+38(044)1234567'}, "level 4")
academy.show_info()
# Main_building = Building("Main building", {'country': 'Ukraine', 'city': 'Kyiv', 'street': 'Khreshatik'},
#                     "5", "43", "12")


vasia = Students("Vasilii", 23, "432345", "Geology", "433")
vasia.show_info()
