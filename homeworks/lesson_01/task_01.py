int_val = 5
float_val = 6.7
str_val = 'Привет мир!'
print(int_val, float_val, str_val, sep=', ')

first_input = input('Введите число:')
if first_input.isdigit():
    first_input = int(first_input)
    print('Вы  ввели:', first_input)
else:
    print('Надо вводить только цифры')
second_input = input('Введите строку:')
print('Вы ыыели:', second_input)
third_input = input('Введите большое число: ')
if third_input.isdigit():
    third_input = int(third_input)
    if third_input > 1000000:
        print('Вы ввели действительно большое число', third_input)
    else:
        print('Вы ввели малеьнкое число, а мы просили большое')
else:
    print('Надо вводить только цифры')
fourth_input = input('Введите вторую строку: ')
if fourth_input == second_input:
    print('Можно было включить немного фантазии, вы повторяетесь')
else:
    print('Вы оригинальны, Ваша строка ', fourth_input)