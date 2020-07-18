result_sum = 0
kill_program = 0
while True:
    if kill_program:
        break
    user_string = input('Введите строку чисел, разделенных пробелом: ')
    user_list = user_string.split(' ')
    for itm in user_list:
        try:
            result_sum = result_sum + int(itm)
        except ValueError:
            kill_program = 1
            break
    print(result_sum)
