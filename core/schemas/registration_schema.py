from typing import Union, Optional
from pydantic import BaseModel, ValidationError, validator
from ..settings import RegistrationUtils

class Registration(BaseModel):
    login: str
    email: str
    password: str
    password_repeat: str
    
    
    @validator('password_repeat')
    def passwords_match(cls, password_repeat, values, **kwargs):
        """
        function validation password

        Args:
            password (str): user input password
            values (dict): dict with data for user

        Raises:
            ValueError: password do not match password_repeat
            or
            ValueError: password do not match regular expression

        Returns:
            str: valid password
        """
        # print(password_repeat)
        # print(values)
        # print(kwargs)
                  
        if 'password' in values and password_repeat != values['password']:
            raise ValueError('passwords do not match password_repeat')
        
        if not RegistrationUtils.regular_registration(password=password_repeat):
            raise ValueError('password fo not match regular expression')
        
        return password_repeat
    

class UserEmail(BaseModel):
    email:str

user = Registration(
    login ='samuel colvin',
    email='scolvin@mail.ru',
    password='zxcvbnASD123!',
    password_repeat='zxcvbnASD123!',
)

# print(user)