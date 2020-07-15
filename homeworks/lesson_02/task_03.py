while True:
    user_month = input('Введите номер месяца в году: ')
    if user_month.isdigit():
        user_month = int(user_month)
        if 1 <= user_month <= 12:
            break
        else:
            print('В году только 12 месяцев.')
    else:
        print('Ошибка в числе')

year_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'месяц за номером {user_month} относится к {year_list[user_month-1]}')

year_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима'
}
print(f'месяц за номером {user_month} относится к {year_dict[user_month]}')
