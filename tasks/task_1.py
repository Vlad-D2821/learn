конвертировать bondsOutstanding -> BondsOutstanding
text_before = 'bondsOutstanding'
text_before2 = text_before[:1].upper() + text_before[1:]
print(text_before2)

#--------------#
count_chars = ("hello")
char_count = {}
for symbol in count_chars:
    if symbol in char_count:
        char_count[symbol] += 1
    else:
        char_count[symbol] = 1
print(char_count)