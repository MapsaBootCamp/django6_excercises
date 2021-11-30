import config
from controller import query
from modules import Coustomers, FoodStuff, Manager, Menu, cart, staff

##manager
manager_1 = Manager("mahdi","1381")
admins_data = query.loadall(str(config.Data_Path)+"/admins")
coustomers_data = query.loadall(str(config.Data_Path)+"/coustomers")
food_data = query.loadall(str(config.Data_Path)+"/menu")
history_data = query.loadall(str(config.Data_Path)+"/cart")


print("""


hello wellcome to our resturant


""")
#manager login
flag = False
ans = input("do u have account (y/n)? ")

while ans == "root":

    Manager_ID = input("what is your ID : ")
    Manager_Pass = input("what is the pass : ")

    if Manager_ID == manager_1.ID and Manager_Pass == manager_1.password:

        flag = True
        print (""" 

        wellcome 


        """)

        while flag:

            temp=input("what do u want to do ?(CM,AA,Q) ")

            if temp == "AA":

                admin_name = input("enter ur admin name : ")
                admin_password = input("chose pasword for ur admin : ")
                admin = staff(admin_name,admin_password)
                admin.save()

            elif temp == "Q":

                flag = False
                ans = input("do u have account (y/n)? ")

            else :

                print(temp+" command not found")

## coustomer register
while ans =="n":

            name= input ("enter a name : ")
            password = input("enter a password : ")
            phone_number = input("enter ur phone number : ")

            if query.search(coustomers_data,name,):

                print("name should be uniq , try agin")

            else:

                Coustomer = Coustomers(name,password,phone_number)
                Coustomer.save()
                print("u are registerd now sigin")
                ans = input("do u have account (y/n)? ")

##login for coustomers

while ans == "y":
        while not flag:
            name_1 = input ("enter ur name : ")
            password_1 = input("enter ur password : ")
            if query.sigin(coustomers_data,name_1,password_1):
                print("u are singed in ")
                flag = True
            else :
                print("pls try agin")
                ans = input("do u have account (y/n)? ")

            while flag:
                temp_costume = input("menu(M),history(H),quite(Q)")
                if temp_costume == "H"or "h":
                    for elm in query.search_history(history_data,name_1):
                        print(elm)
                temp_costume = input("menu(M),history(H),quite(Q)")


                if temp_costume == "m" or "M" or "menu":
                    menu1 = Menu(food_data)
                    print(menu1)
                    order = input("what can i get u :(Q) ").split(" ")
                    count = 0
                    while not order == "Q":
                        cart1 = {}
                        food_object = query.search(food_data,order[0])
                        if food_object:
                            count+=int(food_object.price)*order[1]
                            order = input("what else :(Q),(nothing/n)")
                            cart1[order[0]] = order[1]
                            if order == "nothing" or "n":
                                main_cart = cart(name_1,cart1)
                                print(main_cart)
                                temp3 = input("is every thing ok(y/n)")
                                if temp3 == "y":
                                    main_cart.save()
                                    print("ur bill : " + count)
                                elif temp3 == "n":
                                    order = input("what can i get u :(Q) ").split(" ")
                        else :
                            order = input("pls chose from menu (Q)")
                    if order =="q" or "Q":
                        temp_costume = input("menu(m),quite(Q)")

            if temp_costume == "Q" or "q":
                ans = input("do u have account (y/n)? ")
                flag = False

##login for admins

while ans == "admin":

    admin_name = input("enter ur username : ")
    admin_password = input("enter ur password : ")

    if query.sigin(admins_data,admin_name,admin_password):

        print("wellcome " + admin_name)
        goal = input("what do u want to do ?(CM,CH,Q)")
        flag = True

        while goal == "CM":

            temp_admin = input("(add_food),(chanage status),Q=(go back): ")

            if temp_admin == "add_food" or "add" or "add food" or "addfood":

                new_food_name = input("enter your food name : ")

                if query.search(food_data,new_food_name):

                    print("this food all ready exsist on menu")

                ##Add food
                else : 

                    price = input("enter a price")
                    about_food = input("chose a category: ")
                    status = input("what is the status of food ")
                    new_food = FoodStuff(new_food_name,price,about_food,status)
                    new_food.save()

            elif temp_admin == "Cs" or "chanage status":
                food_name = input("enter the food name : ")
                object = query.search(food_data,food_name)
                if object:
                    status = input("True(1),false(2) to change status ")
                    if status == "1":
                        object.status = "true"
                        print("done")
                    if status == "2":
                        print("done")
                        object.status = "false"
                    else : 
                        print("command not found")
            elif temp_admin == "Q":
                goal = input("what do u want to do ?(CM,CH,Q)")


    else:
        goal = input("try agin or press Q to go back")
        if goal == "Q":
            ans = input("do u have account (y/n)? ")
