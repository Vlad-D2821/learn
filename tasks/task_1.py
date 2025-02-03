# конвертировать bondsOutstanding -> BondsOutstanding
text_before = 'bondsOutstanding'
text_before2 = text_before[:1].upper() + text_before[1:]
print(text_before2)


count_chars = "hello"

char_count = {}

for symbol in count_chars:
    if symbol in char_count:
        char_count[symbol] += 1
    else:
        char_count[symbol] = 1

print(char_count)



def sum_positive(number):
    total = 0
    for i in number:
        if i > 0:
            total += i
    return total
print(sum_positive([1, -4, 7, 12, -3]))


numbers = [3, 5, 2, 8, 10]
total = 0
for num in numbers:
    total += num
print(total)


numbers = [2, 3, 4]
total = 1
for num in numbers:
    total *= num
print(total)


numbers = [5, 12, 8, 3, 25, 7]
max_number = max(numbers)
print(max_number)


numbers = [5, 12, 8, 3, 25, 7]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)


numbers = [9, 3, 15, 2, 8, 7]
min_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
print(min_number)


numbers = [9, 3, 15, 2, 8, 7]
min_number = min(numbers)
print(min_number)


numbers = [4, 7, 10, 3, 6, 8, 1]
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num
print(total)


total = 0
for num in range(1, 101):
    if num % 3 == 0 or num % 5 == 0:
        total += num
print(total)


numbers = [2, 5, 10, 15, 17, 18]
max_number = 0
for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)


string = "madam"
if string == string[::-1]:
    print('Это строка палиндром')
else:
    print('Это строка не палиндром')



n = int(input('Введите число: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} = {factorial}")


n = int(input('Введите число: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 2
print(f"Двойной факториал числа = {factorial}")

n = int(input('Введите число: '))
summa = 0
start = 2 if n % 2 == 0 else 1
while start <= n:
    summa += start
    start += 2
print(f"Сумма чисел одной четности = {summa}")


