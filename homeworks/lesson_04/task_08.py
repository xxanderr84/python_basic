def my_reverse(reverse_list):
    i = 0
    direction = 1
    while True:
        yield reverse_list[i]
        i = i + 1 * direction
        if i == len(reverse_list) - 1:
            direction = -1
            continue
        if i == 0:
            direction = 1


k = 0
my_list = [1, 2, 3, 4, 5]
for itm in my_reverse(my_list):
    print(itm)
    k = k + 1
    if k > 15:
        break
