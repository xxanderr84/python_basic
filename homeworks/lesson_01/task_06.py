while True:
    user_input = input('Введите количество секунд: ')
    if user_input.isdigit():
        break
    else:
        print('Ошибка в числе')
user_input = int(user_input)
hours_ = int(user_input/3600)
user_input = user_input - hours_*3600
minutes_ = int(user_input/60)
user_input = user_input - minutes_*60
seconds_ = user_input
print(f'{hours_:02}:{minutes_:02}:{seconds_:02}')
