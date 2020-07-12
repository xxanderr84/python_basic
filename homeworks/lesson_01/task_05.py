while True:
    user_input_1 = input('Введите значение выручки: ')
    if user_input_1.isdigit():
        break
    else:
        print('Ошибка в числе')
while True:
    user_input_2 = input('Введите значение издержек: ')
    if user_input_2.isdigit():
        break
    else:
        print('Ошибка в числе')
cash = float(user_input_1)
tax = float(user_input_2)
if cash > tax:
    print('У Вас фирма работает с прибылью')
    profit = (cash - tax) / cash
    while True:
        population = input('Введите численность фирмы: ')
        if population.isdigit():
            population = int(population)
            break
        else:
            print('Неверное число')
    if population > 0:
        profitbyman = (cash - tax) / population
        print(f'Рентабельность Вашей фирмы равна {profit}\n'
              f'Прибыль фирмы на одного сотрудника равна {profitbyman} ')
    else:
        print('Численность должна быть больше 0')
else:
    print('В вашей фирме убытки')