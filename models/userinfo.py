
from pydantic import BaseModel, Field,field_validator

class UserInfoDto(BaseModel):
    firstName : str = Field(...,max_length=25,min_length=3,description="First name of the user",)
    lastName : str  = Field(...,max_length=25,min_length=3,description="Last name of the user")
    age : int = Field(...,ge=18, le=75,description="Description of the user")
    
    @field_validator('age')
    def validate_age(cls,v):
        if (v< 17 or v> 75 ):
            raise ValueError("Age cannot be less than 18 or greater than 75.")
        return v
    

    @property
    def full_name(self)->str:
        return "{} {}".format(self.firstName,self.lastName)