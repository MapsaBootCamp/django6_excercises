# from hashlib import sha256

# def set_password(passw):
#         hash_passw = sha256(b'%i'% passw).hexdigest()
#         print(hash_passw)

# set_password(1234)
# # from model import *
# a=Customer
# print(a.type)
# # a=Customer("sara",11111)
# print(a.password)
# a.Save_customer()
# import mysql.connector
# cnx = mysql.connector.connect(user='asal', password='asal.1651374',
#                                     host='localhost',
#                                     database='resturant')
# cursor=cnx.cursor(prepared=True)
# food =( 3 ,'pepperoni pizza', 85000 ,'hotdog,ham, mushroom,spicial souce')
# add_food="INSERT INTO food (number ,foodname, price, info) VALUES (%s,%s,%s,%s);"

# cursor.execute(add_food , food)
 # cnx.commit()
# from uuid import uuid4


# def generate_id():
#         print(str(uuid4()))
# generate_id()
