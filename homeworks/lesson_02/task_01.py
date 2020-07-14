my_list = [1, 2, 3, 3.4, 'sdfsdf', True, False, 4.5, 'asdfsdafsadfsdf']
i = 0
while i < len(my_list):
    print(f'{i} элемент имеет следующий тип {type(my_list[i])}')
    i += 1
