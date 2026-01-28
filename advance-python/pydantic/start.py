from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime
# ... => is called elipsis in python. 

class Fridge(BaseModel):
    name: str
    model_name: str
    bought_on: str
    warranty_expiry: int = Field(..., lt=4000, gt=2026)
    some_text : str 
    
    @field_validator('some_text')
    def check_num(val, clss):
        if val == "polo app download karein":
            return 'karta hu'
            
        return val
    
f = Fridge(name='asdf', model_name='adf', bought_on='someday', warranty_expiry=2028, some_text='polo app download karein')
