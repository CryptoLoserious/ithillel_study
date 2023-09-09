
######################### Homework 4 #############################

# task_4.1
letter = 0
digit = 0
text = input('Enter any text: ')
for i in text:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
print('Amount of digits =', digit)
print('Amount of letters =', letter)

# task_4.2
text = input('Enter your text: ')
letter = input('Enter your letter to search: ')
letters = 0

for l in text:
    if l == letter:
        letters += 1
print('Letters found: ', letters)

# task_4.3
text = input('Enter your text: ')
find_word = input('Enter word to search: ')
change_word = input('Enter word you want to change: ')

text = text.replace(find_word, change_word)
print('Your new text: ', text)

# task_4.4
sentence = "Hello, world"
print(sentence[2])
print(sentence[-2])
print(sentence[0:5])
print(sentence[0:-2])
print(sentence[::2])
print(sentence[1::2])
print(sentence[::-1])
print(sentence[::-2])

print(len(sentence))

####################  additional tasks  #######################

text = input('Input your text: ')
print(text.capitalize())

digit = 0
count_of_marks = 0
marks = ".,;:!?()[]{}'\""

for i in text:
    if i.isdigit():
        digit += 1
print('Amount of digits =', digit)

for mark in text:
    if mark in marks:
        count_of_marks += 1
print('Marks found: ', count_of_marks)

exclamation_points = 0

for i in text:
    if i == "!":
        exclamation_points += 1
print('Exclamation points: ', exclamation_points)
