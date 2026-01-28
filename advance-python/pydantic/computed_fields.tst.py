from pydantic import BaseModel, computed_field

class Books(BaseModel):
    name: str
    price: float
    discount: float
    
    @computed_field
    @property
    def discounted_price(self) -> int: 
        return self.price * self.discount
    
print(Books(name='some_book', price=22.22, discount=10).discounted_price)