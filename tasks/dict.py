car = {
    "brand": "Ford",
    "model": "Mustang",
    # "year": 1964,
    "is_product": False,
    "gear": {1: "<30", 2: "30-50", 3: "50-70", 4: "70>"},
    "max_speed": 125.5,
    "options": ["conditional", "electric window", "hard ceiling"],
}
print(car)

# company = car["company"]
# print('company: ', company)

# company = car.get("company")
# print('company: ', company)

# company = car.get("company", "Ford Motor Company")
# print('company: ', company)


# 4. Change Values
print('='*100)
print('Change Values:')
print('-'*50)
car["year"] = 2018
print(car)

# 5. Loop Through a Dictionary
print('='*100)
print('Loop Through a Dictionary:')
print('-'*50)
print('Print all keys:')
for item in car:
    print(item)

print('-'*50)
print('Print all values:')
for item in car:
    print(car[item])

print('.'*25)
print('car.values(): ', car.values())
for value in car.values():
    print(value)


print('.'*25)
print('car.items(): ', list(car.items()))
print('car.items(): ', car.items())
for key, value in car.items():
    print('key: ', key)
    print('value: ', value)