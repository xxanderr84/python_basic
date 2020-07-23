def remove_duplicate(error_list):
    tmp_list = []
    duplicate_list = set()
    for itm in my_list:
        if itm in tmp_list:
            duplicate_list.add(itm)
        else:
            tmp_list.append(itm)
    return [itm for itm in error_list if not (itm in duplicate_list)]


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

assert remove_duplicate(my_list) == result, 'remove_duplicate(my_list)'
