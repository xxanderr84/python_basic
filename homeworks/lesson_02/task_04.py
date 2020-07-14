user_str = input('Введите строку с несколькими словами, разделенрную пробелами:\n')
result_list = user_str.split(' ')
i = 0
while i < len(result_list):
    print(f'{i + 1}: {result_list[i][:10]}')
    i += 1
