# # # task_1:
#
# with open("test_1.txt", "w") as test1_file:
#     test1_file.write("first, \nsecond, \nthird, \neleven, \ntwelve, \nJanuary, \nFebruary")
# with open("test_1.txt", "r") as test1_file:
#     content = test1_file.read()
# words = [word.strip(",") for word in content.split()]
#
# with open("test_2.txt", "w") as test2_file:
#     for word in words:
#         if len(word) >= 7:
#             test2_file.write(word + "\n")

# # # task_2
# with open("test_3.txt", "w") as test3_file:
#     test3_file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer."
#                      " The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,"
#                      " And by opposing end them? To die: to sleep; No more; and by a sleep to say we end."
#                      " The heart-ache and the thousand natural shocks That flesh is heir to,"
#                      " 'tis a consummation Devoutly to be wish'd. To die, to sleep")
# with open("test_3.txt", "r") as test3_file:
#     text = test3_file.read()
#     words = [text.strip(".,!*\"@#$%^&+=]") for word in text.split()]
#     print(len(words))
#
# """                                  additional task
# Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.             """
#
def find_word_in_text(text, find_word, new_item ="***"):
    words_in_text = text.split()
    changed_text = [new_item if word.lower() == find_word.lower() in text else word for word in words_in_text]

    count_of_words = len([word for word in changed_text if word == new_item])

    print(f"Amount of changed words: {count_of_words}")

    return " ".join(changed_text)

text = input("Input your text: ")
find_word = input("Input your word for change: ")

new_text = find_word_in_text(text, find_word)
print(f"New text: \n {new_text}")


