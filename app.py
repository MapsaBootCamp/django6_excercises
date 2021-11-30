from configparser import NoOptionError
from logging import currentframe
from controllers import *
import model
from db import *

moshtari=None



print(
        '*******************hey!! welcoom to chichifastfood*****************  \n\n'
)

temp=input( '                admin or customer? A/C:')
temp=temp.upper()

if temp=='C':
    
    ans=input( '\n\n \t\tsign in  or  sign up :')
    if ans=='sign up':
        input_data()
        

        model.Customer(data_list[0],data_list[1])
        
        new=model.Customer(data_list[0],data_list[1])
        new.Save_customer()
        
    elif ans=='sign in':
        input_data()
        old=model.Customer(data_list[0],data_list[1])
        register(old)
        moshtari=old
        print('you are registerd')
        ord=input('Enter 1 to see menu and reserve food  \n Enter 2 to see purchase history:')
        if ord=='1':
            c=Query.Food_query()
            cn=input('press y to continue:')

            if cn=='y':
                Reserve=input('to reserve food press food number:')
                Query.add_to_card( moshtari.username ,reserve=Reserve)
            else:
                exit
        if ord=='2':
            Query.show_history()
else:
    input_data()
    admin=model.Admin(data_list[0],data_list[1])
    register(admin)
    

        


            



            


          


            

        


    
            




