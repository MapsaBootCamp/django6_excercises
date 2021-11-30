import uuid
import settings
import pickle
from DataBase import BaseQuery

class MetaBase(type):
    
    def __init__(self, *args, **kwargs):
        self.query = BaseQuery(self.file_path)
        super().__init__(*args, **kwargs)


class MainUser(metaclass=MetaBase):
    type = None
    file_name = None
    file_path = None


    def __init__(self, username, tel, address):
        self.username = username
        self.tel = tel
        self.address = address
        self.purchase_history = []
        self.status = False  # ordinary user

    def save(self):
        try:
            with open(settings.USER_DATA_PATH / self.file_name, "ab") as db_file:
                pickle.dump(self, db_file)

        except Exception as e:
            print(e)

    def update(self):
        pass


class UserAdmin(MainUser):
    type = "admin"
    file_name = "admins.db"
    file_path = settings.USER_DATA_PATH / file_name

    def __init__(self, username, tel, passw):
        #super().__init__(username, tel)
        self.status = True
        self.passw = passw
    
    @staticmethod
    def _set_password(passw):
        return hash(passw)

    def add_user(self):
        pass

    
class Users(MainUser):

    type = "user"
    file_name = "users.db"
    file_path = settings.USER_DATA_PATH / file_name

    def __init__(self, username, tel, address):
        super().__init__(username, tel, address)


    def add_user(self):
        pass

    
class Product:
    _id = 100

    _category = ['Food', 'Drink', 'Service', 'Zarf']

    def __init__(self, name, price, category):
        self.id = Product.id_gen()
        self.serial_num = uuid.uuid4()
        self.name = name
        self.price = price
        self.category = category

    
    @staticmethod
    def id_gen():
        Product._id += 1
        return Product._id

    def save(self):
        try:
            with open(settings.PRODUCT_DATA_PATH / self.file_name, "ab") as db_file:
                pickle.dump(self, db_file)

        except Exception as e:
            print(e)

    def update(self):
        pass

class Food (Product):

    type = "food"
    file_name = "foods.db"
    file_path = settings.PRODUCT_DATA_PATH / file_name

    def __init__(self, name, price, number):
        super().__init__(name, price,number)

    def add_prod(self):
        pass

 

class Drink(Product):

    type = "drink"
    file_name = "drinks.db"
    file_path = settings.PRODUCT_DATA_PATH / file_name
    
    def __init__(self, name, price, number):
        super().__init__(name, price,number)

    def add_prod(self):
        passtype = "drink"
    file_name = "drinks.db"
    file_path = settings.PRODUCT_DATA_PATH / file_name

class Service(Product):

    type = "service"
    file_name = "services.db"
    file_path = settings.PRODUCT_DATA_PATH / file_name
    
    def __init__(self, name, price, number):
        super().__init__(name, price, number)

    def add_prod(self):
        pass


class Zarf(Product):

    type = "zarf"
    file_name = "zarfha.db"
    file_path = settings.PRODUCT_DATA_PATH / file_name
   
    def __init__(self, name, price, number):
        super().__init__(name, price, number)

    def add_prod(self):
    
        pass