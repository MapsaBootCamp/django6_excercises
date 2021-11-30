import pickle
import config
from typing import  Generator

from controller import query

class Manager:

    def __init__(self,manager_ID,password) -> None:
        self.ID = manager_ID
        self.password = password


    def add_admins(self,name ,password ):
        admin = staff(name,password)
        admin.save()

class BaseUers:

    type = None
    def __init__(self, name ,password ) -> None:
        self.name = name
        self.password = password


    def save(self):
        with open(str(config.Data_Path)+self.type , "ab") as file :
            pickle.dump(self,file)


class staff (BaseUers):

    type = "/admins"


    def check_history():
        pass


class Coustomers(BaseUers):
    type = "/coustomers"
    def __init__(self, name, password , phone_number) -> None:
        super().__init__(name, password)
        self.number = phone_number


class FoodStuff(BaseUers):
    type = "/menu"

    def __init__(self, name,price,about_food,status) -> None:
        self.name = name
        self.price = price
        self.about_food = about_food
        self.status = status 

##menu 

class Menu :
    def __init__(self,input_list:Generator) -> None:
        self.list = input_list
    

    def __str__(self) -> str:
        resualt = "[ name   price  about_food    \n"
        for elm in self.list:
            if elm.status == "true":
                resualt +=" "+ str(elm.name) + "   "+str(elm.price) + "  " +str(elm.about_food)
                resualt += "\n"
        return resualt


class cart(BaseUers):

    type = "/cart"

    def __init__(self,name,food:dict) -> None:
        self.food = food
        self.name = name
    
    def __str__(self) -> str :
        result = "[" + self.name +"\n"+"  "+"food_name  "+ "quntity"+"\n"
        for k,v in self.food:
            result+=(k,"  ",v,"\n")
        return result


        
        