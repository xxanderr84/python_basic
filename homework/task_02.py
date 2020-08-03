from abc import abstractmethod


class Clothes:
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    __v = 0

    @property
    def size(self):
        return self.__v

    @size.setter
    def size(self, size: int):
        if 0 < size < 100:
            self.__v = size
        else:
            raise Exception('Не верный размер пальто')

    @property
    def consumption(self):
        return self.__v/6.5 + 0.5


class Costume(Clothes):
    __h = 0

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, height: int):
        if 0 < height < 100:
            self.__h = height
        else:
            raise Exception('Не верный размер костюма')

    @property
    def consumption(self):
        return 2*self.__h + 0.3


test = Coat()
test.size = 45
print(test.consumption)
