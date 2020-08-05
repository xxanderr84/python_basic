class Equipment:
    name = ''
    __model = ''
    __id = ''

    def __init__(self, name: str, model: str, id: str):
        self.__id = id
        self.name = name
        self.__model = model

    @property
    def model(self):
        return self.__model

    @property
    def inventory(self):
        return self.__id


class Printer(Equipment):
    __print_speed: int

    def __init__(self, name: str, model: str, id: str, speed: int):
        super().__init__(name, model, id)
        self.__print_speed = speed

    @property
    def speed(self):
        return self.__print_speed


class Scanner(Equipment):
    __dpi: int

    def __init__(self, name: str, model: str, id: str, dpi: int):
        super().__init__(name, model, id)
        self.__dpi = dpi

    @property
    def dpi(self):
        return self.__dpi


class Xerox(Equipment):
    __scan_speed: int

    def __init__(self, name: str, model: str, id: str, speed: int):
        super().__init__(name, model, id)
        self.__scan_speed = speed

    @property
    def speed(self):
        return self.__scan_speed


class Stock:
    __equipment = []
    name = ''

    def __init__(self, name: str, equipments: list):
        self.name = name
        self.__equipment.extend(equipments)

    def add_equipment(self, equipment: Equipment):
        try:
            if self.__equipment.index(equipment):
                return False
        except ValueError:
            self.__equipment.append(equipment)
            return True

    def remove_equipment(self, equipment: Equipment):
        self.__equipment.remove(equipment)
        return True

    def get_equipment(self, inventory: str):
        for itm in self.__equipment:
            if itm.inventory == inventory:
                return itm
        raise Exception(f'{inventory} not in this stock {self.name}')
