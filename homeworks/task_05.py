import random
#создаем файл случайным набором чисел
tmp_list = []
i = 0
while i < random.randint(15, 20):
    tmp_list.append(random.randint(10, 200))
    i = i + 1
tmp_list = [str(itm) for itm in tmp_list]

with open('task_05.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(tmp_list))

#читаем файл и ищем сумму
with open('task_05.txt', 'r', encoding='UTF-8') as file:
    tmp_list = file.read().split(' ')
try:
    tmp_list = [int(itm) for itm in tmp_list]
except ValueError:
    print('Не верное значение')
print(f'Сумма чисепл равана: {sum(tmp_list)}')
