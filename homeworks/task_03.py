class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        new_dict = dict()
        new_dict['wage'] = wage
        new_dict['bonus'] = bonus
        self._income = new_dict


class Position(Worker):
    def get_fullname(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position('Ivan', 'Petrov', 'engineer', 500, 100)
pos2 = Position('Petr', 'Ivanov', 'car-driver', 600, 700)
print(pos.get_fullname())
print(pos.get_total_income())
print(pos2.get_fullname())
print(pos2.get_total_income())
