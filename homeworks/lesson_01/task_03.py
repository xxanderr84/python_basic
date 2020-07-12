while True:
    user_input = input('Введите число n: ')
    if user_input.isdigit():
        break
    else:
        print('Ошибка в числе')
n = int(user_input)
n_str = str(n)
double_n = n_str + n_str
tripple_n = n_str + n_str + n_str
double_n = int(double_n)
tripple_n = int(tripple_n)
result = n + double_n + tripple_n
print(f'{n} + {double_n} + {tripple_n} = {result}')