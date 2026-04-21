from fastapi import FastAPI
from app.models import Car
from app.parking import ParkingLot

app = FastAPI()

lot = ParkingLot()


@app.get("/")
def home():
    return {"message": "Parking Lot API "}

@app.post("/cars")
def add_car(brand: str, color: str):
    car = Car(brand, color)
    lot.park_car(car)
    return {"message": f"{brand} parked successfully"}

@app.get("/cars")
def get_cars():
    return lot.get_cars()

@app.delete("/cars/{brand}")
def delete_car(brand: str):
    removed = lot.remove_car(brand)
    if removed:
        return {"message": f"{brand} removed"}
    return {"error": "Car not found"}
