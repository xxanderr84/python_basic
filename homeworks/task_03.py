surname = []
salary = []

with open('task_03.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        sur_tmp, sal_tmp = line.split(' ')
        surname.append(sur_tmp)
        try:
            salary.append(int(sal_tmp))
        except ValueError:
            print(f'Не верно введен оклад {sur_tmp}')
i = 0
print('Сотрудники с окладом меньше 20000:')
for itm in salary:
    if itm < 20000:
        print(surname[i])
    i = i + 1
print(f'Средний оклад равен: {sum(salary)/len(salary)}')
