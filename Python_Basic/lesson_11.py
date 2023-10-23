# ^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[1).*$
# ^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$
# t_e@s.com
# ^[+]?[380][0-9]{7}$
# "^[a-zA-ZА-Яа-яёЁЇїІіЄєҐґ]+$"

# import re
#
# test_data = ["Vasya Vasya Vasya", "Vasya, Vasya Vasya", "vasya vasya Vasya", "Vasya Vasya", "Vasya Vasya Vasya Vasya"]
# regex = re.compile(r"^[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}\s[A-ZА-ЯЁЇІҐЄ]{1}[a-zа-яёїієґ]{2,10}$")
#
# for item in test_data:
#     print(regex.match(item))

# import re
#
# li = ['0482-37-35-40', '048-730-25-96', '+38-066-295-18-25', '+38-050-499-38-24', '0992879648', '0482-44-29-16',
#       '048-499-22-19', 'hello world', '0482-33-18-85', '38-099-422-25-65', '38-067-222-17-22']
#
# for val in li:
#     if re.findall(r'^[+]?[0-9]{2}-[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$', val) and 10 <= len(val) <= 17:
#         print(val)
#     elif re.findall(r'^[0]{1}[0-9]{9}$', val) and len(val) == 10:
#         print(val)
#     else:
#         print('incorrect number')

##############
###
# r (Read). Файл відкривається для читання. Якщо файл не знайдено, то генерується виняток FileNotFoundError
#
# w (Write). Файл відкривається для запису. Якщо файл відсутній, він створюється. Якщо такий файл вже є,
# то він створюється заново, і відповідно старі дані в ньому стираються.
#
# a (Append). Файл відкривається для запису. Якщо файл відсутній, він створюється.
# Якщо подібний файл вже є, дані записуються в його кінець.
#
# b (Binary). Використовується для роботи з бінарними файлами. Застосовується разом з іншими режимами – w або r.

# # v1
# try:
#     my_file = open("hello.txt", "w")
#     try:
#         my_file.write("Hello")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e:
#     print(e)
#
# # v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("wwwwww")
# #
# #
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("rrrrr\ntttttt\n")

#
# with open("hello.txt", "r") as myfile:
#     # v1
#     # result = myfile.read()
#     # print(result)
#     # v2
#     # result = myfile.readline()
#     # print(result)
#     # result = myfile.readline(3)
#     # print(result)
#     # v3
#     # result = myfile.readlines()
#     # print(result)
#     # v4
#     # for line in myfile:
#     #     print(line, end="")
#     # v5
#     line = myfile.readline()
#     while line:
#         print(line, end="")
#         line = myfile.readline()

# ###
# FILENAME = "notes.txt"
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note: {i + 1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle
# FILENAME = "notes.dat"
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)  # серіалізація
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)  # десеріалізація
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")

##########
##
# import csv
#
# FILENAME = "users.csv"

# # v1
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Anton", "87347864786347869"]
#     writer = csv.writer(file)
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(f"{row[0]} - {row[1]}")

# # v2
# users = [
#     {"name": "John", "phone": "111"},
#     {"name": "Petya", "phone": "222"},
#     {"name": "Vasya", "phone": "333"},
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
#
#     # all users
#     writer.writerows(users)
#
#     # one user
#     user: dict = {"name": "Test", "phone": "555"}
#     writer.writerow(user)
#
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['name'], " - ", row['phone'])

###
##
import os

# os.mkdir("test_folder")

# os.rmdir("test_folder")
#
# file_name = "users.csv"
# if os.path.exists(file_name):
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")

# доп: написати скрипт для видалення всіх файлів вказаної директорії
#
# # відносний шлях - щодо поточної директорії (папки, де знаходиться исходник, який ви запустили)
# with open("f1/f2/test.txt", "w") as myfile:
#     myfile.write("hello world")
# #
# with open("../../test1.txt", "w") as myfile:
#     myfile.write("hello world")
# абсолютний шлях - повний шлях починаючи з диска C://test_folder/...

#####################
#####################################################################
# import json
#
# # json string data
# employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'
#
# # check data type with type() method
# print(type(employee_string))
#
# # convert string to  object
# json_object = json.loads(employee_string)
#
# # check new data type
# print(type(json_object))
#
# # output
# # <class 'dict'>
#
# # access first_name in dictionary
# print(json_object["first_name"])
# #
# # ####################
# employees_string = '''
# {
#     "employees" : [
#        {
#            "first_name": "Michael",
#            "last_name": "Rodgers",
#            "department": "Marketing"
#
#         },
#        {
#            "first_name": "Michelle",
#            "last_name": "Williams",
#            "department": "Engineering"
#         }
#     ]
# }
# '''
#
# data = json.loads(employees_string)
#
# print(type(data))
# # output
# # <class 'dict'>
#
# # access first_name
# for employee in data["employees"]:
#     print(employee["first_name"])
#
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

###############
# import json
# import os
#
# PATH_TO_TODO_LIST = "myTodoList.json"
#
#
# def create_todo_list_json_file(path_to_storage: str) -> None:
#     if not os.path.exists(path_to_storage):
#         with open(path_to_storage, "w", encoding="utf-8") as file:
#             todos_dict: dict = {"todos": []}
#             file.write(json.dumps(todos_dict))
#     else:
#         raise FileExistsError("File already exists!")
#
#
# def get_todo_items(path_to_storage: str) -> dict:
#     with open(path_to_storage, 'r', encoding="utf-8") as file:
#         return json.load(file)
#
#
# def add_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].append(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# def remove_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].remove(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# if __name__ == "__main__":
#     if os.path.exists(PATH_TO_TODO_LIST):
#         print(get_todo_items(PATH_TO_TODO_LIST))
#         # add_todo_item(PATH_TO_TODO_LIST, "second item1")
#         remove_todo_item(PATH_TO_TODO_LIST, "second item1")
#         print(get_todo_items(PATH_TO_TODO_LIST))
#     else:
#         create_todo_list_json_file(PATH_TO_TODO_LIST)
#
# # дописать меню
# # добавить функцию изменения по порядковому номеру (от 1 до ...)
# # протестировать все функции

############
##
# создать телефонную книгу с сохранением в файл txt
# добавление
# изменение контакта
# удаление
# поиск по имени

import os
import sys

CONTACTS_FILE_PATH = "contacts.txt"


def get_contacts(path_to_file: str) -> str:
    if os.path.exists(path_to_file):
        with open(path_to_file, "r", encoding="utf-8") as file:
            content = file.readlines()
            contacts: str = ""
            for i in range(len(content)):
                contacts += str(i + 1) + ". " + content[i]
        return contacts
    raise FileNotFoundError("File not found!")


def add_contact(path_to_file: str, contact: dict) -> None:
    def write_to_file():
        with open(path_to_file, "a", encoding="utf-8") as file:
            file.write(contact.get("name") + " - " + contact.get("phone") + "\n")
    try:
        current_contacts = get_contacts(path_to_file)
        if current_contacts.find(contact.get("phone")) == -1:
            write_to_file()
        else:
            raise Exception(f"Contact with phone number: {contact.get('phone')} already exists!")
    except FileNotFoundError:
        write_to_file()


def modify_contact(path_to_file: str, contact: dict, contact_phone: str) -> None:
    pass


def delete_contact(path_to_file: str, contact_phone: str) -> None:
    pass


def search_contact_by_name(path_to_file: str, contact_name: str) -> None:
    pass


def get_contact_data_from_keyboard() -> dict:
    new_contact = dict()

    contact_name = input("Enter contact name: ")
    contact_phone = input("Enter contact phone: ")
    new_contact["name"] = contact_name
    new_contact["phone"] = contact_phone

    return new_contact


def main():
    while True:
        user_select = int(input("\n1. Add contact"
                                "\n2. Modify contact"
                                "\n3. Delete contact"
                                "\n4. Get all contacts"
                                "\n5. Search contact by name"
                                "\n6. Exit\n"))
        match user_select:
            case 1:
                add_contact(CONTACTS_FILE_PATH, contact=get_contact_data_from_keyboard())
            case 2:
                modify_contact(CONTACTS_FILE_PATH, contact=get_contact_data_from_keyboard(), contact_phone="")
            case 3:
                delete_contact(CONTACTS_FILE_PATH, contact_phone="")
            case 4:
                print(get_contacts(CONTACTS_FILE_PATH))
            case 5:
                search_contact_by_name(CONTACTS_FILE_PATH, contact_name="")
            case 6:
                sys.exit()
            case _:
                raise ValueError("You selected incorrect menu item!")


try:
    main()
except FileNotFoundError as error:
    print(error)
except ValueError as error:
    print(error)
except Exception as error:
    print(error)
