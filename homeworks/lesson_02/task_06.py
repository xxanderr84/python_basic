while True:
    user_n = input('Введите количество товаров: ')
    if user_n.isdigit():
        user_n = int(user_n)
        break
    else:
        print('Ошибка в числе')
properties = ['название', 'цена', 'количесвто', 'ед']
products = []
i = 0
while i < user_n:
    product_dict = {}
    for itm in properties:
        user_property = input(f'Введите {itm} товара: ')
        product_dict[itm] = user_property
    product = (i+1, product_dict)
    products.append(product)
    i += 1

result_dict = {}
for prop in properties:
    tmp_set = set()
    for itm in products:
        tmp_set.add(itm[1][prop])
    result_dict[prop] = tmp_set
print(result_dict)
