class Date:
    __year = 0
    __month = 0
    __day = 0

    def __init__(self, date: str):
        self.__year, self.__month, self.__day = Date.convert(date)

    @classmethod
    def convert(cls, date: str):
        temp = date.split('-')
        if len(temp) != 3:
            raise Exception('wrong string format. needs: "dd-mm-yyyy"')
        year = int(temp[2])
        month = int(temp[1])
        day = int(temp[0])
        if cls.__check_data(year, month, day):
            return year, month, day
        else:
            raise Exception('wrong digits in string.')

    @staticmethod
    def __check_data(year: int, month: int, day: int):
        if 0 > month > 13:
            return False
        if 0 > day > 31:
            return False
        if year < 0:
            return False
        return True

    def __str__(self):
        return f'{self.__day:>02}.{self.__month:>02}.{self.__year:>04}'


if __name__ == '__main__':
    test = Date('1-2-200')
    print(test)
    print(Date.convert('01-02-2005'))
