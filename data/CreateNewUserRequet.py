
from pydantic import BaseModel


class CreateNewUserRequest(BaseModel):
    firstName : str
    lastName:str
    age : int