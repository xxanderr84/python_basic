class DigitError(Exception):

    def __init__(self, txt):
        self.txt = txt


def is_not_number(s: str) -> bool:
    try:
        float(s)
        return False
    except ValueError:
        return True


my_list = []
while True:
    value_1 = input('Введите данные: ')
    try:
        if is_not_number(value_1):
            raise DigitError('Error number')
        value_1 = float(value_1)
        my_list.append(value_1)
    except DigitError:
        print('Это не число')
    exit_1 = input('Продолжаем? (Да/Нет): ')
    if exit_1 == 'Нет':
        print(my_list)
        break
