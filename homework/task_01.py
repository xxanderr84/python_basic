class Matrix:
    __matrix = []
    __row = 0
    __column = 0

    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise Exception('Не верный тип, нужен list')
        len_matrix = list(map(len, matrix))
        maximum = max(len_matrix)
        minimum = min(len_matrix)
        if maximum != minimum:
            raise Exception('Не верный формат матрицы')
        self.__column = minimum
        self.__row = len(matrix)
        self.__matrix = matrix

    def __str__(self):
        result = ''
        for itm in self.__matrix:
            for j in itm:
                result = result + '{:4}'.format(j)
            result = result + '\n'
        return result

    def __add__(self, other):
        if self.__row != other.__row or self.__column != other.__column:
            raise Exception('Складывать можно матрицы только одинакового размера.')
        result = []
        i = 0
        while i < self.__row:
            row = list(map(sum, zip(self.__matrix[i], other.__matrix[i])))
            result.append(row)
            i = i + 1
        return Matrix(result)


test_1 = [[1, 2, 3],
          [2, 4, 6],
          [3, 6, 9],
          [4, 8, 12]]

test_2 = [[5, 6, 7],
          [8, 9, 10],
          [11, 12, 13],
          [14, 15, 16]]

temp = Matrix(test_1)
temp_2 = Matrix(test_2)
print(temp)
print(temp_2)
print(temp + temp_2)
