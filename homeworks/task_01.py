import time


class TrafficLight:
    __color = ''

    def __init__(self):
        self.__color = ''

    def running(self):
        if self.__color == '' or self.__color == 'green':
            self.__color = 'red'
            time.sleep(7)
            pass
        if self.__color == 'red':
            self.__color = 'yellow'
            time.sleep(3)
            pass
        if self.__color == 'yellow':
            self.__color = 'green'
            time.sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
