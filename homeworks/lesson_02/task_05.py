user_list = [7, 5, 3, 3, 2]
my_list = user_list.copy()
while True:
    while True:
        user_n = input('Введите новый элемент рейтинга: ')
        if user_n.isdigit():
            user_n = int(user_n)
            break
        else:
            print('Ошибка в числе')
    position_insert = len(my_list)
    for itm in my_list:
        if itm < user_n:
            position_insert = my_list.index(itm)
            break
        if itm == user_n:
            position_insert = my_list.index(user_n) + my_list.count(user_n)
            break
    my_list.insert(position_insert,user_n)
    print(user_list)
    print(my_list)
    answer = input(f'Продолжим y/n?')
    if answer == 'n':
        break
