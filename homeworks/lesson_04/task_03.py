def my_range(start: int, stop: int) -> None:
    i = start
    while i < stop:
        yield i
        i = i + 1


print(f'{[itm for itm in range(20, 241) if not((itm % 20) and (itm % 21))]}')

