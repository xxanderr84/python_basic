class Car:
    speed = 0.0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed: float, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        self.speed = self.speed + 10
        return 'Машина поехала'

    def stop(self):
        self.speed = 0
        return 'Машина остановилсась'

    def turn(self, direction: str):
        return f'Машина повернула ({direction})'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            raise Exception('Скорость превышена')
        return self.speed


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            raise Exception('Скорость превышена')
        return self.speed


sport_car = SportCar(10, 'red', 'Ferrari')
town_car = TownCar(20, 'blue', 'Lada')
work_car = WorkCar(30, 'black', 'Catafalk')
police_car = PoliceCar(40, 'white', 'Ford')
sport_car.speed = 100
print(f'{sport_car.name}     {sport_car.color}')
print(f'{work_car.go()}   {work_car.stop()}   {work_car.turn("лево")} ')
print(f'{town_car.show_speed()}')
