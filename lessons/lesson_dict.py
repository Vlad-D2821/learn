# phonebook = {
#     "Anna": "38056484848",
#     "Rick": "38049313956",
#     "Mark": "38074637382",
# }
#
# name = input("Введите имя: ")
# if name in phonebook:
#     print(f"Номер телефона для {name}: {phonebook[name]}")
# else:
#     print("Не найдено")
#
#
# dict_1 = {
#     'key1': 'value1',
#     'key2': ['value2', 1, 2, 30],
#     'key3': None,
#     'key5': False,
#     'key4': True
#     }
# print('dict_1---------------', dict_1)
#
#
# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# print('thisdict: ', thisdict)
# print('thisdict: ', thisdict['year'])
# print('thisdict: ', type(thisdict['year']))
#
#
# people = {
#     "Анна": 25,
#     "Борис": 30,
#     "Виктор": 28,
#     "Галина": 35
# }
# people["Дмитрий"] = 27
# people["Борис"] += 1
# del people["Галина"]
# print(people)
#
#
# students = {
#     "Алиса": [85, 90, 78],
#     "Борис": [72, 88, 91],
#     "Виктория": [90, 95, 92],
#     "Глеб": [60, 75, 80]
# }
# students["Дмитрий"] = 88, 76, 93
# students["Глеб"].append(85)
# lowest_student = min(students, key=lambda name: sum(students[name]) / len(students[name]))
# del students[lowest_student]
# print(students)


# dict_1 = {
#     'key1': 'value1',
#     'key2': ['value2', 1, 2, 30],
#     'key3': None,
#     'key5': False,
#     'key4': True
#     }
# print('dict_1---------------', dict_1)
#
# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# print('thisdict: ', thisdict)
# print('thisdict: ', thisdict['year'])
# print('thisdict: ', type(thisdict['year']))
#
# d = {
#     'key': ['value', 'value2'],
#     'key2': {'key2_1': 'value2', 'key3': 'value3_nested'},
#     'key3': 'value3',
#     'key3': 'value3_last',
#     'key3': 'value3_first',
#     }
# # d['key4'] = d['key3']
# print('d---------------', d)
# print(hash(d['key3']))
#
#
# # The dict() Constructor
# print('='*100)
# print('The dict() Constructor:')
# print('-'*50)
# thisdict = dict(brand="Ford", model="Mustang", year=1964)
# print('thisdict: ', thisdict)
# print('thisdict: ', thisdict['year'])
# print('thisdict: ', type(thisdict['year']))
# # note that keywords are not string literals
# # note the use of equals rather than colon for the assignment
# some_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print('some_dict: ', some_dict)
#
# empty_dict = {}
# empty_dict['asdf'] = 'some string'
# empty_dict['asdfe'] = None
# print('empty_dict: ', empty_dict)
# print('empty_dict: ', type(empty_dict))
#
# lst_tpl = [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]
# dict_ = dict(lst_tpl)
# print('dict_---------------', dict_)
# keys = [1, 2, 3, 4]
# values = ['a', 'b', 'c', 'd', 5]
# res_dict = dict(zip(keys, values))
# print('zip(lst_1, lst_2)---------------', list(zip(keys, values)))
# print('res_dict---------------', res_dict)
#
#
# # ## List of the tuples
# print('.'*25)
# print('List of the tuples:')
# tuple_list = [('brand', "Ford"), ("model",  "Mustang"), ("year", 1964)]
# print('tuple_list: ', tuple_list)
# print(dict(tuple_list))
# # print('.'*25)
# list_keys = ['brand', 'model', "year", 'df']
# list_values = ["Ford", 'Mustang', 1964, 'Pavlo']
# lst_ = [1, 2, 3, 4]
# # None should be changed
# sd = zip(list_keys, list_values, lst_)
# print('sd: ', sd)
# print('sd_list: ', list(sd))
# print('sd_dict: ', dict(sd))
# print(dict(zip(list_keys, list_values)))
#
#
# # # Dict generation with the fromkeys() methods (Built-in)
# print('=' * 100)
# print('Dict generation with the fromkeys() methods:')
# print('-'*50)
# # x = ('key1', 'key2', 'key3')
# lst_keys = ['key1', 'key2', 'key3']
# thisdict = dict.fromkeys(lst_keys, 'default value')
# print('thisdict---------------', thisdict)
# thisdict['key1'] = "asdf"
# thisdict['key2'] = 12
# thisdict['key4'] = [12,]
# thisdict['key5'] = {1: 2}
# print('thisdict---------------', thisdict)
#
# # Dict generator (dict comprehension)
# len_list = 7
# some_dict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# thisdict = {item: item ** 2 for item in range(len_list) if item % 2 == 0}
# print(thisdict)
#
# this_dict = {}
# for item in range(len_list):
#     if item % 2==0:
#         this_dict[item] = item**2
# print('this_dict---------------', this_dict)
#
# square = (i*i for i in range(1000))
# print('square---------------', square)
# total = 0
# for i in square:
#     total += i
# print('total---------------', total)
#
# lst_square = [i*i for i in range(1000)]
# print('lst_square---------------', lst_square)
#
#
# # 1. Dictionary Length
# print('='*100)
# print('Dictionary Length:')
# print('-'*50)
# car = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# print(len(car))
#
#
# # 2. Dictionary is empty
# print('='*100)
# print('Check if dictionary empty:')
# print('-'*50)
# car_1 = {}
# print('car_1---------------', car_1)
# print('type of car_1-------', type(car_1))
# print('dir of car_1-------', dir(car_1))
# print('car_1.keys()---------------', car_1.keys())
# if car_1:
#     print('Yes')
# else:
#     print('No')
#
# if len(car_1) > 0:
#     print('Yes, car_1 dictionary has items')
# else:
#     print('No, car_1 dictionary has not items')


#3. Accessing Items
# # print('.'*25)
# car = {
#      "brand": "Ford",
#      "model": "Mustang",
#      "year": 1964,
#      "is_product": False,
#      "max_speed": 125.5,
#      "options": ["conditionar", "elctric window", "hard ceiling"],
#      "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
# }
#
# print('='*100)
# print('Accessing Items:')
# print('-'*50)
# brand = car["brand"]
# print('brand: ', brand)
#
# custom = car.get("custom")
# print('custom: ', custom)

# # print('.'*25)
# # # The get() method (Built-in)
# brand = car.get("brand")
# print('brand: ', brand)
#
# custom = car.get("custom", 'default value')
# if custom is None:
#     print('custom is None')
# print('custom: ', custom)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "is_product": False,
#     "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
#     "max_speed": 125.5,
#     "options": ["conditionar", "elctric window", "hard ceiling"],
# }

# company = car["company"]
# print('company: ', company)

# company = car.get("company")
# print('company: ', company)

# company = car.get("company", "Ford Motor Company")
# print('company: ', company)


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     # "year": 1964,
#     "is_product": False,
#     "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
#     "max_speed": 125.5,
#     "options": ["conditionar", "elctric window", "hard ceiling"],
# }
# print(car)

# company = car["company"]
# print('company: ', company)

# company = car.get("company")
# print('company: ', company)

# company = car.get("company", "Ford Motor Company")
# print('company: ', company)


# 4. Change Values
# print('='*100)
# print('Change Values:')
# print('-'*50)
# car["year"] = 2018
# print(car)
#
# # 5. Loop Through a Dictionary
# print('='*100)
# print('Loop Through a Dictionary:')
# print('-'*50)
# print('Print all keys:')
# for item in car:
#     print(item)
#
# print('-'*50)
# print('Print all values:')
# for item in car:
#     print(car[item])
#
# print('.'*25)
# print('car.values(): ', car.values())
# for value in car.values():
#     print(value)
#
#
# print('.'*25)
# print('car.items(): ', list(car.items()))
# print('car.items(): ', car.items())
# for key, value in car.items():
#     print('key: ', key)
#     print('value: ', value)
#
# #6. Check if Key Exists
# print('='*100)
# print('Check if Key Exists:')
# print('-'*50)
# cheked_key = "model"
# if cheked_key in car:
#     print(f"Yes, {cheked_key} is one of the keys in the car dictionary")
# else:
#     print('No')
#
# if "model" in car:
#     print(f"Yes, {cheked_key} is one of the keys in the car dictionary")
# else:
#     print('No')


# dict_key = "company"
# if dict_key in car:
#     print(f"Yes, {dict_key} is one of the keys in the car dictionary")
# else:
#     print(f"No, {dict_key} key does not exists in the car dictionary")

#7. Adding Items
# print('='*100)
# print('Adding Items:')
# print('-'*50)
# print(car)
# print(len(car))
# car["color"] = "red"
# print(car)
# print(len(car))


# #8. Removing Items
# print('='*100)
# print('Removing Items:')
# print('-'*50)
# #Python Dictionary pop() Method (Built-in)
# print(car)
# print(len(car))
# model = car.pop("model")
# print('model: ', model)
# print(car)
# print(len(car))

# print('.'*25)
# #Python Dictionary popitem() Method (Built-in)
# print('Removing the last item:')
# print(car)
# print(len(car))
# last_item = car.popitem()
# print('last_item: ', last_item)
# print(car)
# print(len(car))

# print('.'*25)
# print('Using "del" method:')
# print(car)
# print(len(car))
# del car["max_speed"]
# print(car)
# print(len(car))


# print('.'*25)
# print('Using "del" method:')
# max_speed = car.get("max_speed")
# del max_speed
# print(car)
# print(len(car))
#
# # 9.Clear a dictionary (Built-in)
# print('='*100)
# print('Clear a dictionary:')
# car.clear()
# car = {}
# print(car)
# print(id(car))
# print(len(car))
# if car:
#     print(f"Yes, car dictionary has items")
# else:
#     print(f"No, car dictionary has not items")

# print('='*100)
# print('Copy a Dictionary:')
# print ('Некорректне копіювання')
# print('-'*50)
# new_car = car
# print(new_car)
# gear_1 = new_car['gear'][1]
# print('gear_1: ', gear_1)
# new_car['color'] = "blue"
# print('new_car: ', new_car)
# print('car: ', car)
# print('id(new_car): ', id(new_car))
# print('id(car): ', id(car))

# print('.'*25)
# print ('Використання методу copy()')
# new_car = car.copy()
# print(new_car)
# gear_1 = new_car['gear'][1]
# print('gear_1: ', gear_1)
# new_car['color'] = "blue"
# print('new_car: ', new_car)
# print('car: ', car)
# print('id(new_car): ', id(new_car))
# print('id(car): ', id(car))


# print('.'*25)
# print ('Використання конструктора словників dict()')
# new_car_2 = dict(car)
# print(new_car_2)
# new_car_2['color'] = "blue"
# print('new_car_2: ', new_car_2)
# print('car: ', car)
# print('id(new_car_2): ', id(new_car_2))
# print('id(car): ', id(car))

# print('.'*25)
# print ('Використання оператора розпаковки **')
# new_car_2 = {**car}
# print(new_car_2)
# new_car_2['color'] = "blue"
# print('new_car_2: ', new_car_2)
# print('car: ', car)
# print('id(new_car_2): ', id(new_car_2))
# print('id(car): ', id(car)

# BUILT-IN METHODS THAT YOU CAN USE ON DICTIONARIES
# 1. Python Dictionary items() Method
# print('='*100)
# print('Python Dictionary items() Method:')
# # The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# print('-'*50)
# x = car.items()
# print('x: ', x)
# x = list(car.items())
# print('x: ', x)
# x = dict(car.items())
# print('x: ', x)


# # 2. Python Dictionary keys() Method
# print('='*100)
# print('Python Dictionary keys() Method:')
# print('-'*50)
# x = car.keys()
# print('x---------------', x)
# print('type of x-------', type(x))
# x = list(car.keys())
# print(x)


# #3. Python Dictionary values() Method
# print('='*100)
# print('Python Dictionary values() Method:')
# print('-'*50)
# x = car.values()
# print('x---------------', x)
# print('type of x-------', type(x))
# x = list(x)
# print(x)


# #4. Python Dictionary setdefault() Method
# print('='*100)
# print('Python Dictionary setdefault() Method:')
# # The setdefault() method returns the value of the item with the specified key.
# # If the key does not exist, insert the key, with the specified value, see example below
# print('-'*50)
# x = car.setdefault("color", "White")
# print('x---------------', x)
# print('car---------------', car)

# # #5. Python Dictionary update() Method
# print('='*100)
# print('Python Dictionary update() Method:')
# print('-'*50)
# car_1 = car.copy()
# car.update({"color": "White"})
# car.update(brand='Shevi', model='M')
# print('car_1: ', car_1)
# print(car)


# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами значения первого и последнего элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
# import json
# dictionary = {
#     "fruits": ["apple", "banana",],
#     "cars": ["bmw", "ford"],
#     "tv": ["lg", "samsung"],
#     "other": ["wallpaper", "fifa"],
#     "boxes": ["23cм", "45см"],
# }
# json_string = json.dumps(dictionary)
# print(json_string)
# items = list(dictionary.items())
# items[0], items[-1] = items[-1], items[0]
# dictionary = dict(items)
# print(dictionary)
#
# del dictionary["cars"]
# print(json_string)
#
# dictionary["new_kay"] = ["new_value"]
# print(dictionary)


# Как получить значение по ключу "marks" словаря student = {"name": "Emma", "class": 9, "marks": 75}
# student = {"name": "Emma", "class": 9, "marks": 75}
# marks = student["marks"]
# print(marks)

# Что выведет этот код?
# p = {"name": "Mike", "salary": 8000}
# print(p.get("age"))

# Как получить "d":sample = {"1":["a","b"], "2":["c","d"]}.
# sample = {"1":["a","b"], "2":["c","d"]}
# d = sample["2"][1]
# print(d)

# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
# Дано
# list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
# list_2 = ["Киев", "Токио", "Минск"]
# Получить
# dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]
# Сгенерировать словарь-шифратор, то есть словарь, где ключ и значение являются символами. Используя словарь, зашифровать/расшифровать введенное сообщение.
# list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
# list_2 = ["Киев", "Токио", "Минск"]
# city_to_country = {}
# for item in list_1:
#     city_to_country["city"] = item.split("-")
#
#
#
dict_ = {
    "fruits": ["apple", "banana",],
    "cars": ["bmw", "ford"],
    "tv": ["lg", "samsung"],
    "other": ["wallpaper", "fifa"],
    "boxes": ["23см", "45см"],
}
adress = id(dict_)
print(adress)
keys_ = list(dict_.keys())
print(keys_)
first_k = keys_[0]
last_k = keys_[-1]
first_v = dict_[first_k]
last_v = dict_[last_k]
print(first_v, last_v)
dict_[first_k] = last_v
dict_[last_k] = first_v
adress = id(dict_)
print(dict_)

#
#
# dict_ = {
#     "fruits": ["apple", "banana",],
#     "cars": ["bmw", "ford"],
#     "tv": ["lg", "samsung"],
#     "other": ["wallpaper", "fifa"],
#     "boxes": ["23см", "45см"],
# }
# adress = id(dict_)
# print(adress)
# items = list(dict_.items())
# print(items)
# items[0], items[-1] = items[-1], items[0]
# print(items)
# dict_new = dict(items)
# print(dict_new)
# adress = id(dict_new)
# print(adress)
# dict_.clear()
# print(dict_)
# dict_.update(dict_new)
# print(dict_)
# adress = id(dict_)
# print(adress)




#
#
# ist_1 = ["Украина-Киев", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
# list_2 = ["Киев", "Токио", "Минск"]
# country_city_l = []
# for item in list_1:
#     country_city = item.split('-')
#     print('country_city---------------', country_city)
#     if country_city[1] in list_2:
#         country_city_l.append(country_city)
# print('country_city_l---------------', country_city_l)
# country_city_d = dict(country_city_l)
# print('country_city_d---------------', country_city_d)
#
#
# list_1 = ["Украина-Киев", "Беларусь-Минск", "Германия-Мюнхен", "Япония-Токио"]
# list_2 = ["Киев", "Токио", "Минск"]
# country_city_l = []
# for item in list_1:
#     country_city = item.split('-')
#     print('country_city---------------', country_city)
#     print('country_city[1]---------------', country_city[1])
#     if country_city[1] in list_2:
#         country_city_l.append(country_city)
#     else:
#         continue
#     print('country_city_l---------------', country_city_l)
# country_city_d = dict(country_city_l)
# print('country_city_d---------------', country_city_d)

# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
# import json
# dictionary = {}
# for num in range(1,11):
#     dictionary[num] = num ** 3
# with open("data.json", "w") as file:
#     json.dump(dictionary, file, indent=4)
# print(dictionary)
# #
# dictionary = {num: num ** 3 for num in range(1, 11)}
# print(dictionary)


# Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
# dictionary = "Hello"
# dictionary = {char: dictionary.count(char) for char in dictionary}
# print(dictionary)

