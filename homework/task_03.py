class Cell:
    __cell_count = 0

    def __init__(self, cell_count: int):
        self.__cell_count = cell_count

    def __add__(self, other):
        return Cell(self.__cell_count + other.__cell_count)

    def __sub__(self, other):
        if self.__cell_count < other.__cell_count:
            raise Exception('Разность меньше нуля, операция не возможна')
        return Cell(self.__cell_count - other.__cell_count)

    def __mul__(self, other):
        return Cell(self.__cell_count*other.__cell_count)

    def __truediv__(self, other):
        return Cell(self.__cell_count // other.__cell_count)

    def __str__(self):
        return self.make_order(self.__cell_count)

    def make_order(self, row: int):
        if row <= 0:
            raise Exception('Количесвто ячеек в ряду должно быть больше 0')
        result = ''
        row_count = self.__cell_count // row
        remainder = self.__cell_count % row
        i = 0
        while i < row_count:
            result = result + '*' * row
            result = result + '\\n'
            i = i + 1
        if remainder == 0:
            return result[:-2]
        result = result + '*' * remainder
        return result


test = Cell(10)
test_2 = Cell(3)
print(test.make_order(5))
print(test + test_2)
print(test - test_2)
print(test * test_2)
print(test / test_2)
