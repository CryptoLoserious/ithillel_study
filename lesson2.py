# # умови
# # v1
# n1 = 10 + 20 * 2 # оператор привласнення "=" відпрацьовує останнім
# n2 = 20
#
# # v2
# n1, n2 = 10, 20 #множинне привласнення
# n1 == n2 #перше дірівнює другому
# n1 != n2 #перше НЕ дорівнює другому
#
# # v3
#
# is_valid = True
# print(is_valid)
# print(not is_valid)
#
# print('hello' in 'hello word')

# # v1
# hours = int(input('Enter hours: '))
# if hours >= 12 and >= 1 and <= 24:
#     print('PM')
# else:
#     print('AM')

# hours = int(input('Enter hours: '))
# if hours >= 12 and hours <= 24:
#     print('PM')
# elif hours >= 1 and hours <= 12:
#     print('AM')
# else:
#     print('Incorrect hours')
#
film_rating = int(input('Input film_rating: '))
if 0 < film_rating <= 5:
    if film_rating == 4 or film_rating ==5:
        print('OK')
    else:
        print('not OK')
else:
    print('Incorrect rating')