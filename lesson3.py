# n1, n2 = 10, 0
# p rint(n1 / n2)

# num = float(input('Enter your number: '))
# print(num)
##########################################################
# try:
#     num1 = int(input('Enter first number: '))
#     num2= int(input('Enter second number: '))
#
#     result  = num1/num2
#     print(f'Result: {result}')
# except ZeroDivisionError as error:
#     print(f"ZerroDivigionError occurred: {error}")
# except ValueError as error:
#     print('Enter only integer number please!')
#     print(f'ValueError')
# except Exception as error:
#     print(f'Exeption occurred: {error}')
# finally:
#     print('End of calculation!')
#
# print('Some text')
##########################################################
# try:
#     name = input('Input your name')
#     if 1 < len(name) <= 20:
#         print(f"Hello: {name}")
#     else:
#         raise Exception('Please enter a valid name!')
# except Exception as e:
#     print(f'Error: {e}')
#########################################################
# try:
#     print('1. Start game\n2. Setting\n3. Saved games\n4. Exit')
#     user_select = int(input('Enter menu number: '))
#
#     #v1
#     if user_select == 1:
#         print('Game started!')
#     elif user_select == 2:
#         print('Setting opened!')
#     elif user_select == 3:
#         print('Saved game opened!')
#     elif user_select == 4:
#         print('Exit...')
#     else:
#         print('Incorrect item menu!')
#
#     #v2
#     match user_select:
#         case 1:
#             print('Game started!')
#         case 2:
#             print('Setting opened!')
#         case 3:
#             print('Saved game opened!')
#         case 4:
#             print('Exit...')
#         case _:
#             print('Incorrect item menu!')
#
# except Exception as e:
#     print(f'Exception: {e}')
#########################################################
# i = 0
#
# while i < 10:
#     print(i, end=" ")
#     i += 1
# print("test")
#########################################################
# i = 0
#
# while True:
#     i += 1
#
#     if i == 5:
#         print('Continue...')
#         continue
#     if i >= 10:
#         print('Break...')
#         break
#     print(i)
#
# print('After while!')
#########################################################
# sum_num = 0
# count = 0
# try:
#     while True:
#         try:
#             num = int(input('Enter number: '))
#             if num == 0 and count == 0:
#                 print('enter the number!')
#                 continue
#             if num == 0:
#                 print('end...')
#                 break
#
#             sum_num += num
#             count += 1
#         except ValueError as e:
#             print('Enter numbers only!')
#
#     average = sum_num / count
#     print(f'Sum_num: {sum_num}')
#     print(f'average: {average}')
#     print(f'count: {count}')
# except Exception as e:
#     print(e)
######################### HOMEWORK #########################
# #lesson1
# while True:
#         try:
#             print('Choose a day of the week: \n1. First day\n2. Second day\n3. Third day\n4. Fourth day \n5. Fifth day\n6. Sixth day\n7. Seventh day')
#             user_select = int(input('Enter a day of the week: '))
#
#             match user_select:
#                 case 1:
#                     print('First day is Monday')
#                     break
#                 case 2:
#                     print('Second day is Tuesday')
#                     break
#                 case 3:
#                     print('Third day is Wednesday')
#                     break
#                 case 4:
#                     print('Fourth day is Thursday')
#                     break
#                 case 5:
#                     print('Fifth day is Friday')
#                     break
#                 case 6:
#                     print('Sixth day is Saturday')
#                     break
#                 case 7:
#                     print('Seventh day is Sunday')
#                     break
#                 case _:
#                     print('Incorrect a day of the week. Repeat your choice!')
#         except ValueError as e:
#                 print('Enter numbers only. Repeat your choice!')

# #lesson2
# try:
#     while True:
#         try:
#             print('Enter two numbers. ')
#             num1 = int(input('Enter first number: '))
#             num2 = int(input('Enter second number: '))
#             if num1 == num2:
#                 print('Good, your numbers are equal')
#                 break
#             if num1 >= num2:
#                 print(num2, num1)
#                 break
#             if num1 <= num2:
#                 print(num1, num2)
#                 break
#         except ValueError as e:
#             print('Enter numbers only! Repeat the input.')
#             continue
# except ValueError as error:
#     print('Enter only integer number please!')
#     print(f'ValueError')
# except Exception as error:
#     print(f'Exception occurred: {error}')
# print('End of the calculation =)')

# lesson3
user_select = 0
try:
    while True:
        try:
            print('Enter two numbers and select an operation between them ("+" , "-" , "/" , "*" )')
            number1 = int(input('Enter first number: '))
            number2 = int(input('Enter second number: '))
            operation = input('Select operation: "+" , "-" , "/" , "*" :')
            if operation == '+' or operation == '"+"':
                print(number1, '+', number2, '=', number1+number2)
                break
            elif operation == "-" or operation == '"-"':
                print(number1, '-', number2, '=', number1-number2)
                break
            elif operation == "/" or operation == '"/"':
                print(number1, '/', number2, '=', number1/number2)
                break
            elif operation == "*" or operation == '"*"':
                print(number1, '*', number2, '=', number1*number2)
                break
        except ZeroDivisionError as error:
            print(f"ZerroDivigionError occurred: {error}, Repeat the input!")
        except ValueError as e:
            print('Enter numbers only! Repeat the input.')
            continue
except ValueError as error:
    print('Enter only integer number please!')
    print(f'ValueError')
except Exception as error:
    print(f'Exception occurred: {error}')
print('End of the calculation =)')





