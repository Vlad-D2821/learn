# from telebot import TeleBot
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
#
# TOKEN =
#
# bot = TeleBot(TOKEN)
#
# @bot.message_handler(content_types=["start"])
# def get_text_message(message):
# @bot.message_handler(content_types=[""])
#
#
# bot.infinity_polling()
import string
from typing import List

# def process_list(numbers):
#     # Получаем только четные числа
#     even_numbers = [num for num in numbers if num % 2 == 0]
#
#
#
#     # Находим сумму всех чисел
#     total_sum = sum(numbers)
#
#
#     # Твой код здесь
#     # Проходишь по списку numbers, заполняешь even_numbers и total_sum
#
#     return even_numbers, total_sum
#
#
# # Пример использования
# numbers = [1, 2, 3, 4, 5, 6]
# print("Четные числа:", process_list(numbers)[0])
# print("Сумма чисел:", process_list(numbers)[1])


# def find_max(numbers):
#     # Твой код здесь
#     return max(numbers)
#
# # Пример использования
# numbers = [3, 5, 2, 8, 1]
# print("Самое большое число:", find_max(numbers))


# def filter_strings(strings):
#     # Твой код здесь
#     result = []
#     for i in strings:
#         if i.startswith("A") or i.startswith("a"):
#             result.append(i)
#     return result
#
# strings = ["Apple", "banana", "Avocado", "grape", "apricot"]
# print("Строки, начинающиеся на 'А':", filter_strings(strings))
#
#
#
# # Пример использования
# strings = ["Apple", "banana", "Avocado", "grape", "apricot"]
# print("Строки, начинающиеся на 'А':", filter_strings(strings))


# Дано список list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# за допомогою ліст компрехеншин згенерувати список
# 1) list_2 - який містить чотні (кратні 2) числа list_2 = [2, 4, 6, 8]
# 2) list_3 - який містить числа кратні 3 list_3 = [3, 6, 9]

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_2 = [num for num in list_1 if num % 2 == 0]
# print (list_2)
# list_3 = [num for num in list_1 if num % 3 == 0]
# print(list_3)

# Дано список fruits = ['apple', 'banana', 'melon', 'pineapple']
# за допомогою ліст компрехеншин згенерувати список
# 1) list_2 - який містить слова що починаються з букви 'a' результат list_2 = ['apple']

# fruits = ['apple', 'banana', 'melon', 'pineapple']
# for i in fruits:
#     if "a" in i:
#         print(i)

# fruits = ['apple', 'banana', 'melon', 'pineapple']
# list_2 = [fruit for fruit in fruits if fruit.startswith("a")]
# print(list_2)


# Дано список fruits = ['apple', 'banana', 'melon', 'pineapple']
# за допомогою ліст компрехеншин згенерувати список
# 1) list_2 - який містить слова написані у верхньому регістрі результат list_2 = ['APPLE', 'BANANA', 'MELON', 'PINEAPPLE']

# fruits = ['apple', 'banana', 'melon', 'pineapple']
# list_2 = [fruit.upper() for fruit in fruits]
# print(list_2)

# Дано список bad_lists = ['Adobe', 'Audience', 'Manager', 'Ds', 'This', 'There', 'These']
# дано фільтруючий список filter_list = ['This', 'Ds', 'There', 'These']
# за допомогою ліст компрехеншин згенерувати список
# у відповідності із фільтруючим результат повинен бути result_list = ['Adobe', 'Audience', 'Manager']

# bad_lists = ['Adobe', 'Audience', 'Manager', 'Ds', 'This', 'There', 'These']
# filter_list = ['This', 'Ds', 'There', 'These']
# filter_list_2 = [bad_lists for bad_lists in bad_lists if bad_lists not in filter_list]
# print(filter_list_2)


# Имеется два списка. Проверить все ли элементы второго списка присутствуют в первом списке.
# list_1 = ['car', 'apple', 'book', 'laptop', 'photo', 'notebook',]
# list_2 = ['apple', 'book', 'car']
# result = set(list_1).issubset(list_2)
# print (result)
# missing_piece = set(list_1) - set(list_2)
# list_2.extend(missing_piece)
# print(list_2)


# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
# list_1 = ['1', '1']
# list_2 = [list_1[0]] + [0] * 100 + [list_1[-1]]
# print(list_2)
# print(len(list_2))

# list_1 = ['2']
# for list_1 in range(2, 92, 2):
#     print(list_1)

# Пользователь вводит число. Определить, содержит ли список данное число x.
# Вывести информационное сообщение содержит или не содержит ;

# list_1 = ['1', '2', '3', '28', '51', '99']
# num_1 = input('Введите любое число: ')
# if num_1 in list_1:
#     print('Ваше число', num_1, 'совпало со списком')
# else:
#     print(num_1, 'Неверное число')



# Дан произвольный список. Представьте его в обратном порядке.
# list_1 = ['apple', 'car', 'laptop', 'lemonade', 'bag']
# list_1.reverse()
# print(list_1)

# Поменять местами самый большой и самый маленький элементы списка; без ключа макс выводил число 5
# list_1 = ['0', '1', '5', '10', '15', '20', '25']
# num_min = min(list_1, key=int)
# num_max = max(list_1, key=int)
# min_index = list_1.index(num_min)
# max_index = list_1.index(num_max)
# list_1[min_index], list_1[max_index] = list_1[max_index], list_1[min_index]
# print(list_1)



# list_2 = ['melon', 'pineapple', 'car', 'file']
# string_min = min(list_2, key=len)
# print(string_min)
# string_max = max(list_2, key=len)
# print(string_max)

# Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение;
# list_1 = ['laptop', 'tv', 'table', 'tv', 'car', 'car']
# repeated = set([word for word in list_1 if list_1.count(word) > 1])
# print(repeated)

# Найдите сумму и произведение элементов списка. Результаты вывести на экран;
# list_1 = [1, 7, 10, 15, 99, 85]
# print(sum(list_1))
# product_of_elements = 1
# for num in list_1:
#     product_of_elements *= num
#     print(f"произведение элементов", {product_of_elements})


# def goes_after(word: str, first: str, second: str) -> bool:
#     # your code here
#     if first in word and second in word and first != second:
#         first_index = word.find(first)
#         second_index = second.find(second)
#         return first_index + 1 < len(word) and word[first_index + 1] == second
#     return False
#
#
# print("Example:")
# print(goes_after("world", "w", "o"))
#
# # These "asserts" are used for self-checking
# assert goes_after("world", "w", "o") == True
# assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("list", "l", "o") == False
# assert goes_after("", "l", "o") == False
# assert goes_after("list", "l", "l") == False
# assert goes_after("world", "d", "w") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
#
#
# def goes_after(word: str, f: str, s: str) -> bool:
#     return f + s in word if f != s else False
#

# students = ('Alice', 'Vlad', 'Pasha')
# for student in students:
#     print(student)
#     for char in student:
#         print(char)

# import turtle
# joe = turtle.Turtle()
# joe.forward(100)
# joe.left(60)
# joe.forward(100)

numbers = [
    [43, 2, 77, 48, 24, 9, 3, 65, 41, 42, 10, 75, 14, 69, 61],
    [20, 47, 69, 38, 2, 49, 76, 42, 81, 34, 10, 47, 76, 85, 81, 72],
    [92, 46, 25, 61, 75, 40, 87, 9, 52, 77, 0, 11, 25],
    [48, 74, 81, 71, 32, 82, 39, 74, 37, 72, 15],
    [8, 26, 12, 71, 5, 83, 75, 30, 34, 77]
]
max_number = max([max(number) for number in numbers])

print(max_number)




# the_str = "The quick, brown fox: jumps over the lazy dog! Dog not amused."
# punctuation = [char for char in the_str if char in string.punctuation]
# print(punctuation)


def sum_numbers(text: str) -> int:
    # text.split(): Разделяем текст на слова, используя пробел как разделитель
    words = text.split(" ")
    # word.isdigit(): Проверяем, является ли каждое слово числом.
    # int(word): Преобразуем слова, которые являются числами, в целые числа.
    # sum(): Суммируем все найденные числа.
    return sum(int(word) for word in words if word.isdigit())


# print("Example:")
# print(sum_numbers("hi"))
#
# # These "asserts" are used for self-checking
# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#         sum_numbers(
#             "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#         )
#         == 3755
# )
# assert sum_numbers("5 plus 6 is") == 11
# assert sum_numbers("") == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


n = int(input('Введите число: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 2
print(f'Двойной факториал числа = {factorial}')