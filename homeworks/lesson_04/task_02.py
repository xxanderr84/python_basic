my_list = [10, 20, 30, 40, 50]
tmp_list = my_list.copy()
tmp_list.pop(0)
new_list = [itm for itm in tmp_list]
print(new_list)

