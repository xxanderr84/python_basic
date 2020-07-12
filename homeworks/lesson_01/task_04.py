while True:
    user_input = input('Введите число: ')
    if user_input.isdigit():
        n = int(user_input)
        if n > 0:
            break
        else:
            print('Нужно положительное число')
    else:
        print('Ошибка в числе')
max_ = 0
while n > 0:
    if n % 10 > max_:
        max_ = n % 10
    n = int(n/10)
print(f'Самая большая цифра в числе {user_input} равна {max_}')
