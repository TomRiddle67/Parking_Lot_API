from fastapi import FastAPI
from app.models import Car
from app.parking import ParkingLot

app = FastAPI()

lot = ParkingLot()

@app.get('/')
def home():
    return {'message': 'Parking Lot API is running'}

@app.post('/cars')
def add_car(brand, color):
    car = Car(brand, color)
    lot.park_car(car)
    return {f"message: {brand} parked succesfully"}
