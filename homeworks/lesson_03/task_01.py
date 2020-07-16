def my_divide(val1: float, val2: float):
    if val2:
        return val1 / val2
    return 'Делить на ноль нельзя'


while True:
    user_val1 = input('Введите делимое: ')
    try:
        user_val1 = float(user_val1)
        break
    except ValueError:
        print('Неверное число')

while True:
    user_val2 = input('Введите делитель: ')
    try:
        user_val2 = float(user_val2)
        break
    except ValueError:
        print('Неверное число')

print(f'Результат: {my_divide(user_val1, user_val2)}')
