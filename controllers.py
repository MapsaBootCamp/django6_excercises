from logging import error, exception, raiseExceptions
from model import *


data_list=[]
def input_data():
    name=input('pleas enter your fullname:')
    passwrd=int(input('enter your password Maximum 5 charector:'))
    data_list.append(name)
    data_list.append(passwrd)
    return(data_list)

def register( user ):
    cnx = mysql.connector.connect(user='asal', password='asal.1651374',
                                    host='localhost',
                                    database='resturant')
    cursor=cnx.cursor(buffered=True)
    if user.type==Customer:
        query1= "SELECT  username  FROM customer WHERE (username = '%s' );"
        query2="SELECT password FROM customer WHERE (password= '%s') ;"
    else:
        query1= "SELECT  username  FROM admin WHERE (username = '%s' );"
        query2="SELECT password FROM admin WHERE (password= '%s') ;"
    
    cursor.execute(query1, user.username)
    cnx.commit()
    row = cursor.fetchone()
    print(row)
    if row:
        query="SELECT password FROM CUSTUMER WHERE (password= '%s') ;"
        cursor.execute(query2, user.password)
        cnx.commit()
        row = cursor.fetchone()
        print(row)
        if row:
            print('you are registerd')
        else:
            raise exception('password incorrect')
    else:
        raise exception('username incorrect')

  