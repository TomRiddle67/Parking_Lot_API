class Car:
    def __init__(self,brand, color):
        self.brand = brand   
        self.color = color
    def __str__(self):
        return f"{self.brand} is a {self.color} car"
regular_car = Car('Peaguot', 'Blue')
print(regular_car)