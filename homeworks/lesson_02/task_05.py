user_list = [7, 5, 3, 3, 2]
my_list = user_list.copy()
while True:
    user_n = input('Введите новый элемент рейтинга: ')
    if user_n.isdigit():
        user_n = int(user_n)
        break
    else:
        print('Ошибка в числе')

itm_exist = 0
for itm in my_list:
    if itm == user_n:
        itm_exist = 1
        break

if itm_exist:
    my_list.insert(my_list.index(user_n) + my_list.count(user_n), user_n)
else:
    my_list.append(user_n)

my_list.sort()
my_list.reverse()
print(user_list)
print(my_list)
