def my_func(val1: float, val2: float, val3: float) -> float:
    tmp_list = [val1, val2, val3]
    tmp_list.sort()
    return tmp_list[1] + tmp_list[2]


while True:
    user_val1 = input('Введите первое число: ')
    try:
        user_val1 = float(user_val1)
        break
    except ValueError:
        print('Неверное число')

while True:
    user_val2 = input('Введите второе число: ')
    try:
        user_val2 = float(user_val2)
        break
    except ValueError:
        print('Неверное число')

while True:
    user_val3 = input('Введите третье число: ')
    try:
        user_val3 = float(user_val3)
        break
    except ValueError:
        print('Неверное число')

print(f'Результат: {my_func(user_val1, user_val2, user_val3)}')
