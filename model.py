from controller import Admin_query

from controller import food_data

from controller import orders



class Admin(Admin_query):

    def __init__(self,username,password):

        self.username=username
        self.password=password

    def Admin_checker(self):
        try:
            if Admin_query.admin_check(self.username,self.password) or self.username=='Admin' and self.password=='Root':
                return True
            else:
               return False
        except:
            'internal error between line 13 and 19 in model'
    
    def define_admin(id,UserName,PassWord):
        Admin_query.define_admin(id, UserName, PassWord)
    
    def add_user(id,name,family,phone,Address):
        Admin_query.define_user(id, name, family, phone, Address)
    
    def edit_user_data(id,name, family, phone, address):
        Admin_query.edit_user(id,name, family, phone, address)



class food(food_data):
    
    def add_food_data(food_id,food_name_,food_material_,food_price_,food_reservasion_):
        food_data.insert_food(food_id,food_name_, food_material_, food_price_, food_reservasion_)

    def remove_food_data(food_id):
        food_data.remove_food(food_id)
    
    def update_food_data(food_id,food_name_, food_material_, food_price_, food_reservasion_):
        food_data.update_food(food_id, food_name_, food_material_, food_price_, food_reservasion_)


class order(orders):
    
    def order(costumer_id,food_id,count):
        orders.register_order(costumer_id, food_id, count)

    


class root_admin(Admin_query):

    def define_admin_by_root(id,user_name,password):
        Admin_query.define_admin(id, user_name, password)


    

    





