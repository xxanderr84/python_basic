def int_func(user_string: str) -> str:
    """
    Функция делает первый символ строки прописным
    user_string: строка
    :return: строка с первой прописной буквой
    """
    result_string = ''
    i = 0
    while i < user_string.__len__():
        if i == 0:
            result_string = user_string[0].upper()
        result_string = result_string + user_string[i]
        i = i + 1
    return result_string


def int_super_func(long_string: str) -> str:
    """
    Функция делает все первые буквы в словах прописными
    long_string: строка
    :return: строка с первыми прописными буквами
    """
    tmp_list = long_string.split(' ')
    i = 0
    while i < tmp_list.__len__():
        tmp_list[i] = int_func(tmp_list[i])
        i = i + 1
    return ' '.join(tmp_list)


user_string = input('Введите строку: ')
print(int_super_func(user_string))
