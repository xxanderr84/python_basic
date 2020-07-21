from functools import reduce

my_list = [itm for itm in range(100, 1001, 2)]
print(my_list)
result = reduce(lambda x, y: x*y, my_list)
print(result)
