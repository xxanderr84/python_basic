from random import randint
my_list = [randint(0, 200) for _ in range(0, randint(15, 20))]
print(my_list)
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)

