result = []
with open('task_01.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        result.append(line.count(' ') + 1)
print(f'Количестов строк: {result.__len__()}')
for idx, itm in enumerate(result, 1):
    print(f'в строке {idx} имеется {itm} слов')
