weight = int(input('Введите вес посылки (кг): '))
a = 50
if weight <= 2:
    print('Стоимость доставки ', a)
if 2 < weight < 10:
    for i in range(2, 10):
        if weight == i:
            a = a + (20 * (i - 2))
            print('Стоимость доставки ', a)
if weight >= 10:
    print('Стоимость доставки ', a * 4)
