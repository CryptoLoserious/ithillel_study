import re

# # # task_1
# home_phone_numbers = ['38(0642)32-98-81', '999999-999', '38(0642)329891', '99999x9999', '380642329981', '0642-32-98-81',
#       '(0642)32-98-81', '(0642)32-98-81', '0642329881']
#
# for val in home_phone_numbers:
#     if (re.match(r'[0-9]{1}[0-9]{9}', val) or
#         re.match(r'[0-9]{2}[(]{1}[0-9]{4}[)]{1}[0-9]{2}[-]{1}[0-9]{2}[-]{1}[0-9]{2}', val) or
#         re.match(r'[0-9]{2}[(]{1}[0-9]{4}[)]{1}[0-9]{6}', val) or
#         re.match(r'[0-9]{2}[(]{1}[0-9]{4}[)]{1}[0-9]{11}', val)
#         and
#         len(val) == 10 or
#         len(val) == 13 or
#         len(val) == 14 or
#         len(val) == 15 or
#         len(val) == 17):
#
#         print('correct')
#     else:
#         print('incorrect')

# # # task_2
# mob_phone_numbers = ['+38(099)123-45-67', '999999-999', '+80991234567','+38(099)1234567', '99999x9999', '+380991234567',
#                      '099-123-45-67', '(099)123-45-67','+38(599)1234567', '0991234567']
#
# for val in mob_phone_numbers:
#     if (re.match(r'\d{10}', val) or
#             re.match(r'[+]{1}3\d{1}[(]{1}0\d{2}[)]{1}\d{3}[-]{1}\d{2}[-]{1}\d{2}', val) or
#             re.match(r'[+]{1}3\d{1}[(]{1}0\d{2}[)]{1}\d{7}', val) or
#             re.match(r'[+]{1}3\d{1}0\d{9}', val)
#             and
#             len(val) == 10 or
#             len(val) == 13 or
#             len(val) == 14 or
#             len(val) == 17):
#
#         print('correct')
#     else:
#         print('incorrect')

# # task_3
# mob_phone_numbers = ['test1@gmail.com', 'test2@qqqqqqqqqqqq.ua', 'test3@www.com', 'test4@i.comq']
#
# for val in mob_phone_numbers:
#     if re.search(r'@\w{1,}\.\w{1,3}$', val):
#
#         print('correct')
#     else:
#         print('incorrect')
#
# # task_4:
#
# first_second_name = ['Vasya', 'Ivan Petrovich Fedorov', 'Oleg Uriuovich', 'Irina Maksymivna Popova', 'Oleksandr Sergeevich Sergeev']
#
# for name in first_second_name:
#     if re.match(r'\D{2,20}\s\D{2,20}\s\D{2,20}', name):
#         print(name)
#
"""                                              additional task   
                                
Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)"""

passwords = ['jdI3dR1(-', '12345', 'sjU653odK@f:', 'qwerty', '7%fvUI8drTyh!vr632', 'fheuc543%#^@ejvevKBEC92hre34JH!^)']

for passw in passwords:
    if re.match(r'^([a-z]*[A-Z]*\d*\W*).{8,16}$', passw):
        print(f"{passw} It is correct password :)")
    else:
        print('There is no normal password here!')

