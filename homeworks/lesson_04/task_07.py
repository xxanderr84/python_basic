def fact(end: int):
    i = 1
    result = 1
    while i < end + 1:
        result = result * i
        i = i + 1
        yield result


while True:
    end_value = input('Введите конечное значение: ')
    try:
        end_value = int(end_value)
        break
    except ValueError:
        print('Не верное число')

for itm in fact(end_value):
    print(itm)
