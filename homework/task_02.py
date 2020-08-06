class MyZeroDivisionError(Exception):

    def __init__(self, txt):
        self.txt = txt


while True:
    value_1 = input('Введите делимое: ')
    value_2 = input('Введите делитель: ')
    try:
        value_1 = float(value_1)
        value_2 = float(value_2)
        if value_2 == 0:
            raise MyZeroDivisionError('Zero division error, try another number')
        print(f'Частное: {value_1/value_2}')
    except MyZeroDivisionError:
        print('Плохие числа, попробуйте другие')
    except ValueError:
        print('Нужно вводить числа, а рне строки')
    exit_1 = input('Продолжаем? (Да/Нет): ')
    if exit_1 == 'Нет':
        break
