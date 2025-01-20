def sum_numbers(text: str) -> int:
    # text.split(): Разделяем текст на слова, используя пробел как разделитель
    words = text.split(" ")
    # word.isdigit(): Проверяем, является ли каждое слово числом.
    # int(word): Преобразуем слова, которые являются числами, в целые числа.
    # sum(): Суммируем все найденные числа.
    return sum(int(word) for word in words if word.isdigit())


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
        sum_numbers(
            "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
        )
        == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
