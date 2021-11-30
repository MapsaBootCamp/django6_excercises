from typing import Dict
import setting
import pickle
from db import BaseQuery
from uuid import uuid4
import bcrypt



class MetaBase_1(type):
    
    def __init__(self, *args, **kwargs):
        self.db_obj = BaseQuery(self.file_path)
        super().__init__(*args, **kwargs)



class BaseUser(metaclass=MetaBase_1):
    user_type=None
    file_name=None
    file_path=None

    def __init__(self,username:str,userpass:str)->None:
        """
        tabe sazande Baseuser hast ke username va password
         ra migirad va sheie ra misazad
        """
        self.username=username
        self.password=self.__setpassword(userpass)
        # self.id=str(uuid4())

    def save(self):
        """
        save kardan etelaat dar file database baray userha
        """
        with open (self.file_path , "ab") as file:

            pickle.dump(self,file)       
            
                 
    @staticmethod
    def __setpassword(userpass:int):
        """
        tabe sakhtan password hast 
        """
        return bcrypt.hashpw(userpass, bcrypt.gensalt())


class Admin(BaseUser):
    """
    admin asli:
    username:ali
    password:22
    """


    user_type="Admin"
    file_name="admin.db"
    file_path=setting.User_Dir/file_name
    def __init__(self,username:str,password:str)->None:
        """
        tabe sazande admin hast ke username va password
         ra migirad va sheie ra misazad
        """
        super().__init__(username,password)

class Customer(BaseUser):
    """
    customer asli:
    username:mehdi
    password:16
    """

    user_type="Customer"
    file_name="customer.db"
    file_path=setting.User_Dir/file_name
    def __init__(self,username:str,password:str):
        """
        tabe sazande customer hast ke username va password
         ra migirad va sheie ra misazad
        """
        super().__init__(username,password)


class Foods(metaclass=MetaBase_1):
    file_path=setting.Food_Dir/"food.db"
    def __init__(self,name:str,price:int,activate:str,inf:str)->None:
        """
        tabe sazande food hast ke name , price , active bodan , etelat ghaza
         ra migirad va sheie ra misazad
        """

        self.name=name
        self.price=price
        self.activate=activate
        self.inf=inf
    def save(self):
        """
        baray save kardan etelat dar file db
        """
        with open (self.file_path , "ab") as file:
            pickle.dump(self,file)            
