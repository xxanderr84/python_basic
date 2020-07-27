import json

average_profit = 0
firm_dict = dict()
average_dict = dict()
i = 0

with open('task_07.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        tmp_list = line.split('   ')
        print(tmp_list)
        try:
            firm_profit = float(tmp_list[2]) - float(tmp_list[3])
            if firm_profit > 0:
                average_profit = average_profit + firm_profit
                i = i + 1
            firm_dict[tmp_list[0]] = firm_profit
        except ValueError:
            continue
average_profit = average_profit / i
average_dict['average_profit'] = average_profit
result = [firm_dict, average_dict]
print(result)
with open('task_07.json', 'w', encoding='UTF-8') as file:
    json.dump(result, file)
