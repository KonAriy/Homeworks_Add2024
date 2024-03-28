weight = int(input('Введите вес посылки (кг): '))
rub = 50
if weight <= 2:
    rub = 50
if weight < 10:
    rub = 50 + (weight - 2) * 20
else:
    rub = 200

print('Стоимость досьавки составит: ', rub, 'руб.')
