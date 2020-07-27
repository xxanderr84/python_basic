while True:
    user_string = input('Вводите данные:')
    file = open('task_01.txt', 'a', encoding='UTF-8')
    if user_string == '':
        file.close()
        break
    user_string = user_string + '\n'
    file.write(user_string)
