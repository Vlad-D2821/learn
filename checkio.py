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

#-------------------------------#

def checkio(words: str) -> bool:
    # add your code here
    lyrics = words.split()
    count = 0
    for word in lyrics:
        if word.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

#-------------------------#

def beginning_zeros(a: str) -> int:
    # your code here
    return len(a) - len(a.lstrip("0"))


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
