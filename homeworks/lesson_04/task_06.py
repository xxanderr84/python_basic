from random import randint
from itertools import count
from itertools import cycle


def my_count(start: int):
    j = start
    while True:
        yield j
        j = j + 1


my_list = [randint(0, 20) for _ in range(0, randint(5, 10))]
while True:
    start_value = input('Введите стартовое значение: ')
    try:
        start_value = int(start_value)
        if 0 < start_value < 15:
            break
        print('Желательно число от 1 до 14')
    except ValueError:
        print('Не верное значение!')

for itm in my_count(start_value):
    if itm > 15:
        break
    print(itm)

i = 0
print(my_list)
for itm in cycle(my_list):
    print(itm)
    i = i + 1
    if i > 15:
        break
