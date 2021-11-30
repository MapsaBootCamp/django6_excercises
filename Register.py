from mongoengine import *
from hashlib import sha256
from enum import unique
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField




connect('Resturant')


class insert_sing_up(Document):
    username = StringField(Required=True, min_length=8, unique=True)
    pssword = IntField(Required=True, min_length=8)
    Type = StringField(Required=True)
   
    
    def _set_hash(self):
        hash_pass = sha256(b'%d'%self.pssword).hexdigest()
        return hash_pass

    def user_list(self):
        User_list = []
        for user in User1.object:
            User_list.append(user)
        return User_list


User = insert_sing_up()
User.username = input('please enter your username: ')
User.pssword = int(input("enter yor password :"))
User.Type = input("Enter your type: ")
if not User.Type == "Admin" and User.Type == "Customer":
    raise ValueError("please enter Admin or Customer! ")
User.save()

User1 = insert_sing_up.__objects.get()
# User_list = []
# for user in User1:
#     User_list.append(user)





class Sing_in(insert_sing_up, Document):

    print("WELCOME TO PARSA_DONALT", end="\t\t\t")

    def __init__(self, username):
        self.username = username
        
    
    
    
    def check_user(self):
        if self.username in insert_sing_up.user_list:
            return None
        else:
            return insert_sing_up
        
        

    

    
username = input("enter your username: ")    
password = int(input("Enter your password: "))
Type = input("enter your Type: ")        
