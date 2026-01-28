from pydantic import BaseModel

class Car(BaseModel):
    model: str
    price: float

class Vehicle(BaseModel):
    name: str
    price: float
    units_sold: int 
    vehicle_type: Car
    

some_body = {
    'name': 'some car',
    'price': 69.69,
    'units_sold': 420,
    'vehicle_type': { # see we are nesting dat 'Car' class to validate 
        'model':'ferrari f204',
        'price': 342412341234.34
    }
}

v = Vehicle(**some_body)
print(f'{v=}') 
    


