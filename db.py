import model
import mysql.connector


class Query(object):
    
    cnx = mysql.connector.connect(user='asal', password='asal.1651374',
                                        host='localhost',
                                        database='resturant')
    def  Food_query ():
        cursor=Query.cnx.cursor()
        query="SELECT * FROM food;"
        cursor.execute(query)
        row = cursor.fetchall()
        for item in row:
            print(item)

    def add_to_card( username,reserve=None):
         cursor=Query.cnx.cursor(prepared=True)
         query="INSERT INTO orderd (customer ,ord ) values(%s ,%s) "
         add_data=(username,reserve )
         cursor.execute(query , add_data)
         Query.cnx.commit()
    def show_history():
        cursor=Query.cnx.cursor()
        query="SELECT foodname FROM food INNER JOIN orderd ON food.number=orderd.ord"
        cursor.execute(query)
        row = cursor.fetchall()
        for item in row:
            print(item)
    






                    





    

