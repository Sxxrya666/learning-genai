from pydantic import BaseModel, field_validator, model_validator

class SignUp(BaseModel):
    email: str
    password: str
    confirm_password: str
    
    
    @field_validator('confirm_password')
    def check_pass_eq(val, cls):

        if cls.data['password'] == val:
            return 'password match!!'
        return val

s = SignUp(email='a@a.com', password='abc', confirm_password='abc')