while True:
    user_n = input('Введите количество элементов списка: ')
    if user_n.isdigit():
        user_n = int(user_n)
        break
    else:
        print('Ошибка в числе')

i = 0
user_list = []
while i < user_n:
    tmp = input(f'Введите {i} элемент списка: ')
    user_list.append(tmp)
    i = i + 1

result_list = []
i = 0
while i < user_n:
    if i + 1 == user_n:
        result_list.append(user_list[i])
        break
    result_list.append(user_list[i+1])
    result_list.append(user_list[i])
    i = i + 2
print(f'Стартовый список: {user_list}')
print(f'Итоговый список: {result_list}')
