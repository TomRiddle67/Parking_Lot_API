from app.models import Car

class ParkingLot:
    def __init__(self):
        self.cars = []

    def park_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return [{
            'brand': car.brand, 'color': car.color}
            for car in self.cars
        ]

    def remove_car(self, brand):
        for car in self.cars:
            if car.brand == brand:
                self.cars.remove(car)
                return True
            return False