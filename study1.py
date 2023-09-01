# # lesson 1
# a = int(input('Input first number: '))
# b = int(input('Input second number: '))
# c = int(input('Input third number: '))
#
# summa = a + b + c
# mult = a * b * c
#
# print('Summa =', summa,'\n' 'Multiplication =', mult)
#
# # lesson 2
# a = int(input('Input bigger diagonal: '))
# b = int(input('Input smaller diagonal: '))
#
# area = (a * b) / 2
#
# print('Area of a rhombus = ', area)
#
# # lesson 3 (V1)
# number = int(input('Input your four-digit number: '))
#
# n1 = number // 1000
# n2 = number // 100 % 10
# n3 = number // 10 % 10
# n4 = number % 10
#
# result = (n1 * n2 * n3 * n4)
#
# print('Digit of your number =', result)

# lesson 3 (V2)
number = input('Input your number: ')
result = 1
for i in number:
    result *= int(i)

print('Digit of your number =', result)