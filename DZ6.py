# задание 1
# from time import sleep
#
# class TrafficLight:
#     __color = 'Красный'
#
#     def running(self):
#         print('светофор горит красный')
#         sleep(7)
#         print('Светофор горит желтым')
#         sleep(2)
#         print('Светофор горит зеленым')
#         sleep(3)
# traf_light = TrafficLight()
# traf_light.running()

#задание 2
#
# class Road:
#     def __init__(self, length, width):
#         self._lenght = length
#         self._width = width
#
#     def calc(self):
#         return f'Масса равна: {(self._lenght * self._width * 25 * 0.05) / 1000} т'
#
# round1 = Road(5000, 20)
# print(round1.calc())

# Задание 3

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'profit': wage, 'bonus': bonus}
# class Position(Worker):
#     def get_full_name(self):
#         return f'{self.name}{self.surname}'
#
#     def get_full_profit(self):
#         return f'{sum(self._income.values())}'
# worker1 = Position('Ben', 'Morgan', 'Doc', {'profit': 12, 'bonus': 78})
# print(worker1.get_full_name())
# print(worker1.get_full_profit())

# 4 задание
# class Car:
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f'New car: {self.name} color: {self.color} police? {self.is_police}')
#     def go(self):
#         print(f'Car {self.name} go')
#
#     def stop(self):
#         print(f'Car {self.name} stop')
#
#     def show_speed(self):
#         print(f'Car {self.name} speed {self.speed}')
# class TownCar(Car):
#     def show_speed(self):
#         print(f'Car {self.name} speed {self.speed} {"Превывшение сокрости" if self.speed >60 else "Скорость не превышена"}')
#
# class WorkCar(Car):
#     def show_speed(self):
#         print(f'Car {self.name} speed {self.speed} {"Превывшение сокрости" if self.speed >40 else "Скорость не превышена"}')
#
# class SportCar(Car):
#     '''Спортивный автомобиль'''
#
# class PoliceCar(Car):
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
# town_car = TownCar('Bus', 'Yellow', 58)
# town_car.show_speed()
#
# # 5 задание
# class Stationary:
#     def __init__(self, title='Может рисовать'):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationary):
#     def draw(self):
#         print(f'Запуск отрисовки ручкой {self.title}')
#
# class Pencil(Stationary):
#     def draw(self):
#         print(f'Запуск отрисовки карандашом {self.title}')
#
# class Handler(Stationary):
#     def draw(self):
#         print(f'Запуск отрисовки маркером {self.title}')
#
# st = Stationary()
# st.draw()
#
# pen = Pen('Parker')
# pen.draw()
#
# pencil = Pencil('Pop')



