n1 = int(input('Input first number: '))
n2 = int(input('Input second number: '))
n3 = int(input('Input third number: '))

value = input('Select choice: "MIN", "MAX", "MID_SUM": ')

#MIN
if value == "MIN":
    if n1 < n2 and n1 < n3:
        print('MIN = ', n1)
    elif n2 < n1 and n2 < n3:
        print('MIN = ', n2)
    elif n3 < n1 and n3 < n2:
        print('MIN = ', n3)
# elif value != "MAX" and value != "MIN" and value != "MID_SUM":
#     print('Input integer number!')

#MAX
    if value == "MAX":
        if n1 > n2 and n1 > n3:
            print('MAX = ', n1)
        elif n2 > n1 and n2 > n3:
            print('MAX = ',n2)
        elif n3 > n1 and n3 > n2:
            print('MAX = ',n3)
# elif value != "MAX" and value != "MIN" and value != "MID_SUM":
#     print('Input integer number!')

#MID_SUM
if value == "MID_SUM":
    print('MID_SUM = ', ((n1 + n2 + n3)/3))
elif value != "MAX" and value != "MIN" and value != "MID_SUM":
    print('Input correct amounts!')