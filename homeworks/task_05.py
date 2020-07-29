class Stationery:
    title = ''

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Рисует ручка: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Рисует карандаш: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Рисует маркер: {self.title}'


pen = Pen('Ручка-штучка')
pencil = Pencil('Карандаш-Крым наш!')
handle = Handle('Маркер-сталкер')

print(f'{pen.draw()}')
print(f'{pencil.draw()}')
print(f'{handle.draw()}')
