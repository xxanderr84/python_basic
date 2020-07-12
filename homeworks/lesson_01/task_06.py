while True:
    user_input_1 = input('Введите стартовый километраж: ')
    if user_input_1.isdigit():
        break
    else:
        print('Ошибка в числе')
while True:
    user_input_2 = input('Введите цель: ')
    if user_input_2.isdigit():
        break
    else:
        print('Ошибка в числе')
a = int(user_input_1)
b = int(user_input_2)
result = 0
while b >= a * 1.1 ** result:
    print(f'{result + 1} день: {a * 1.1 ** result:.2f}')
    result = result + 1;
print(f'{result + 1} день: {a * 1.1 ** result:.2f}')
print(f'Необходимо {result+1} дней')
