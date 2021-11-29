from model import Admin ,food
from controller import food_data,user
from model import root_admin
from model import order
class View:
     
    def __init__(self,type_):

        self.type_=type_
       
        if self.type_=='admin':
            login.admin()

        if self.type_=='user':
            login.user()


class login():

    def admin():
            
            print('hello admin')

            user_name=input('please enter your user name :')

            pass_word=input('please enter your user password :')
            
            admin_runner=Admin(user_name, pass_word)
            
        
            if admin_runner.Admin_checker()==True:
                print(' ')
                print('Hello you loggined as an amdin\n')
                print(' ')
                print('for define an admin (just by root admin) : add amin ')

                print('For see menu enter : Menu \n')
                
                print('For add food  : add food \n')

                print('For remove food enter rm food \n')
                
                print('for see users enter : users \n')

                print('for edit menu enter : Menu Edit\n')

                print('for define users : add user \n')
                
                print('for edit food of menu : edit menu ')

                print('for edit user : edit user ')


                print('\n')

                request=input('what do you want to do ?  \n ')

                if request=='menu' or request=='Menu':
                       show_data.show_menu_()

                elif request=='users' or request=='Users':
                    show_data.show_users()

                elif request=='add user' or request=='Add User' or request=='Add user':
                    user_.define_user()

                elif request=='add food' or request=='Add Food' or request=='Add food':
                    admin.add_food_by_admin()
                
                elif request=='rm food' :
                    admin.remove_food_by_admin()
                
                elif request=='add admin':
                    try:
                        if user_name=='Admin' and pass_word=='Root':
                            admin_id=input('please enter amin id : ')
                            UserName=input('please enter user name : ')
                            PassWord=input('please enter password')
                            root_admin.define_admin(admin_id, UserName, PassWord)
                            print('successflly registered . ')
                        else:
                            print('just root admin is able to manage other admins .... ')
                    except Error as e :
                            print(e)

                elif request=='edit menu' or request=='Edit Menu':
                    admin.edit_menu_by_admin()
                
                elif request=='edit user':
                    user_.edit_user()

                else:
                    print('mistake command ...')
         
            else:
                print('you are not admin  , please try agian ...')

    def user():
        print('hello you loggind as user , you can just see the menu and order ...')
        user_order.order()


class user_order(order):

    def order():
        print('this is list of food : ')
        show_data.show_menu()
        list_of_order =[]
        while True:
            food=input('whitch do you want ? ')
            count=int(input('how many do you want ?'))
            costumer_id=input('please enter your id : ')
            n=input('do want to continue order ? (yes/no) :')
            order.register_order(costumer_id, food, count)
            if n=='no':
                print('thank you for buying food ...')
                break
            else:
                continue




class show_data(food_data,user):
     
    def __init__(self):
        pass  

    def show_menu_():
        print('this is food menu : ')
        food_data.show_menu()
    
    def show_users():
        print('this is list of users :')
        user.show_user()

class user_():
    
    def define_user():
        id=input('please enter user id :')
        name=input('please enter name of user :')
        family=input('please enter users family :')
        phone=input('please enter users phone :')
        address=input('please enter users address :')
        try:
            Admin.define_user(id, name, family, phone, address)    

            print('sucsessfully defined . ')
        except:
            'Error in Internal Services ... '

    def edit_user():
        print('Now you are editing user ...')

        id=input('whitch user do you want to edit ? please enter id  :')

        name=input('please enter name of user :')

        family=input('please enter users family :')

        phone=input('please enter users phone :')

        address=input('please enter users address :')

        Admin.edit_user(id, name, family, phone, address)

        print('successfully edited. ')





class admin(food):

    
    def add_food_by_admin():

        food_id=int(input('please enter food id :'))
        name=input('please enter food name :')
        material=input('whats the material of this food ? ')
        price=int(input('please enter price : '))
        food_reservasion=input('is it possible to reserve or no ?')

        try:
            food.add_food_data(food_id, name, material, price, food_reservasion)

            print('food Successfully registred . ')

        except :
            raise Exception('some problems in adding data... check functions ...')
    
    def remove_food_by_admin():
        try:
            food_id=input('please enter food id  :  ')
            food.remove_food_data(food_id)
            print(' ')

            print('removed successflly . ')
        
        except:
            raise Exception('Error internal services ... ')
    
    def edit_menu_by_admin():

        food_id=input('please enter food id : ')
        food_name=input('whats food name ? ')
        food_material=input('whats food material : ')
        food_price=input('please enter price  : ')
        food_reservasion=input('please enter can custumers order or no ? ')

        try:
            food.update_food_data(food_id, food_name, food_material, food_price, food_reservasion)
            print('edit successful.')
        except:
            raise Exception('Error in internal services ...')



User_type=input('please enter who are you admin or user ?  : ')

run_view=View(User_type)

run_login=login()