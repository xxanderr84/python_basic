class Road:
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._width = width
        self._length = length

    def count_mass(self, mass: float, depth: float):
        return self._width * self._length * mass * depth


while True:
    try:
        length = float(input('Введите длину полотна: '))
        width = float(input('Введите ширину полотна: '))
        mass = float(input('Введите массу полотна: '))
        depth = float(input('Введите толщину полотна: '))
        break
    except ValueError:
        print('Не верно ввели данные, повторите еще раз')
road = Road(length, width)
print(road.count_mass(mass, depth))
