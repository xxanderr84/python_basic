class Complex:
    __real_part = 0.0
    __imaginary_part = 0.0

    def __init__(self, real: float, imaginary: float):
        self.__real_part = real
        self.__imaginary_part = imaginary

    def __str__(self):
        if self.__imaginary_part == 0:
            return f'{self.__real_part}'
        temp = '+'
        if self.__imaginary_part < 0:
            temp = '-'
        return f'{self.__real_part} {temp} {abs(self.__imaginary_part)}i'

    def __add__(self, other):
        c = Complex(0, 0)
        c.__imaginary_part = self.__imaginary_part + other.__imaginary_part
        c.__real_part = self.__real_part + other.__real_part
        return c

    def __sub__(self, other):
        c = Complex(0, 0)
        c.__imaginary_part = self.__imaginary_part - other.__imaginary_part
        c.__real_part = self.__real_part - other.__real_part
        return c

    def __mul__(self, other):
        c = Complex(0, 0)
        c.__imaginary_part = self.__imaginary_part * other.__real_part + self.__real_part * other.__imaginary_part
        c.__real_part = self.__real_part * other.__real_part - self.__imaginary_part * other.__imaginary_part
        return c

    def __truediv__(self, other):
        c = Complex(0, 0)
        if other.__imaginary_part == 0 and other.__real_part == 0:
            raise ZeroDivisionError()
        c.__real_part = (self.__real_part * other.__real_part + self.__imaginary_part * other.__imaginary_part) /\
                        (other.__imaginary_part * other.__imaginary_part + other.__real_part * other.__real_part)
        c.__imaginary_part = (self.__imaginary_part * other.__real_part - self.__real_part * other.__imaginary_part) / \
                             (other.__imaginary_part * other.__imaginary_part + other.__real_part * other.__real_part)
        return c


a = Complex(1, 3)
b = Complex(-1, -2)
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
