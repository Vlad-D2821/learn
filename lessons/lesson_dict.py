phonebook = {
    "Anna": "38056484848",
    "Rick": "38049313956",
    "Mark": "38074637382",
}

name = input("Введите имя: ")
if name in phonebook:
    print(f"Номер телефона для {name}: {phonebook[name]}")
else:
    print("Не найдено")


dict_1 = {
    'key1': 'value1',
    'key2': ['value2', 1, 2, 30],
    'key3': None,
    'key5': False,
    'key4': True
    }
print('dict_1---------------', dict_1)


thisdict = dict(brand="Ford", model="Mustang", year=1964)
print('thisdict: ', thisdict)
print('thisdict: ', thisdict['year'])
print('thisdict: ', type(thisdict['year']))


people = {
    "Анна": 25,
    "Борис": 30,
    "Виктор": 28,
    "Галина": 35
}
people["Дмитрий"] = 27
people["Борис"] += 1
del people["Галина"]
print(people)


students = {
    "Алиса": [85, 90, 78],
    "Борис": [72, 88, 91],
    "Виктория": [90, 95, 92],
    "Глеб": [60, 75, 80]
}
students["Дмитрий"] = 88, 76, 93
students["Глеб"].append(85)
lowest_student = min(students, key=lambda name: sum(students[name]) / len(students[name]))
del students[lowest_student]
print(students)
