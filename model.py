from uuid import uuid4
from hashlib import sha256
import mysql.connector
import mysql





class BaseUser(object):
    type=None
    data=None
    db_table=None

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self._set_password(password)
        
        self.id = self._generate_id()

    @staticmethod
    def _generate_id():
        return str(uuid4())


    @staticmethod
    def _set_password(passw):
        hash_passw= sha256(b'%d'% passw).hexdigest()
        return hash_passw


    def Save_customer(self):    
        cnx = mysql.connector.connect(user='asal', password='asal.1651374',
                                    host='localhost',
                                    database='resturant')
        cursor=cnx.cursor(prepared=True)
        # print('connect')

        Customer_data=(self.username,self.password,self.type,
        self.id)
        add_customer="INSERT INTO customer (username, password, type, id) VALUES (%s, %s, %s, %s);"

        cursor.execute(add_customer , Customer_data)
        cnx.commit()




class Admin(BaseUser):
    type='admin'



class Customer(BaseUser):
    type='customer'
    reserve=None

    


class FoodMenu():
    pass