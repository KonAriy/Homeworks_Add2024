number = int(input('Введите число: '))
a = 1
if number == 1:
    print('Единица не является простым числом.')
else:
    while a != number:
        a = a + 1
        if a == 2:
            print(a)
        elif a == 3:
            print(a)
        elif a % 2 == 0 or a % 3 == 0:
            continue
        else:
            print(a)


