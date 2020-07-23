from random import randint


def my_range(start: int, stop: int):
    i = start
    while i < stop:
        yield i
        i = i + 1


def task_function(new_list):
    return [new_list[i] for i in my_range(1, len(new_list)) if new_list[i] > new_list[i-1]]


my_list = [randint(0, 200) for _ in range(0, randint(15, 20))]
print(my_list)
print(task_function(my_list))


check_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [12, 44, 4, 10, 78, 123]
assert task_function(check_list) == result_list, "task_function([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])"
