dict_lec = ['(л)', '(пр)', '(лаб)']
result = dict()

with open('task_06.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp_list = line.split(' ')
        sum_h = 0
        for itm in tmp_list:
            for i in dict_lec:
                itm = itm.replace(i, '')
            try:
                sum_h = sum_h + int(itm)
            except ValueError:
                continue
        result[tmp_list[0].replace(':', '')] = sum_h
print(result)
