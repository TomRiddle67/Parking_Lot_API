class Car:
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color

    def __str__(self):
        return f"{self.brand} is a {self.color} car"

