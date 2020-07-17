def int_func(user_string: str) -> str:
    result_string = ''
    i = 0
    while i < user_string.__len__():
        if i == 0:
            result_string = user_string[0].upper()
        result_string = result_string + user_string[i]
        i = i + 1
    return result_string


def int_super_func(long_string: str) -> str:
    tmp_list = long_string.split(' ')
    i = 0
    while i < tmp_list.__len__():
        tmp_list[i] = int_func(tmp_list[i])
        i = i + 1
    return ' '.join(tmp_list)


print(int_func('sdfsdfdsfsdfdsf'))
print(int_super_func('dsfsdf fdsfsd fdsfds fdsfdsfsdfdsfsdfdsf fdsfwewer fq'))