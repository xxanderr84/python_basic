rus_eng = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
           }
tmp_list = []

with open('task_04.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        for itm in rus_eng.items():
            line = line.replace(itm[0], itm[1])
        tmp_list.append(line)
print(tmp_list)

with open('task_04r.txt', 'w', encoding='UTF-8') as new_file:
    new_file.write(''.join(tmp_list))
