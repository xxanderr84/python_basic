def my_func(x: float, y: int, **kwargs):
    if kwargs['method'] == 'star':
        return x ** y
    if kwargs['method'] == 'cycle':
        i = 0
        result = 1
        while i > y:
            result = result / x
            i = i - 1
        return result
    return 'Не выбран спопоб расчета'


while True:
    user_x = input('Введите первое число (x): ')
    try:
        user_x = float(user_x)
        break
    except ValueError:
        print('Неверное число')

while True:
    user_y = input('Введите второе число: ')
    try:
        user_y = int(user_y)
        if user_y > 0:
            print('Число должно быть отрицательным')
            continue
        break
    except ValueError:
        print('Неверное число')

print(f'Результат: {my_func(user_x, user_y, method="star")}')
print(f'Результат: {my_func(user_x, user_y, method="cycle")}')
