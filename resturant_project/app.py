import contoroller as ct

def menu_customer(username:str):
    """
    menu customer va tavanei hay k darad s
    
    """



    print('''
    1-sabeghe kharid
    2-sefaresh ghaza
    3-back
    '''
    )

    option1=input("entekhab konid :")

    if option1== "1":
        ct.sabeghe_kharid_customer(username)
        opt=input("press any key to continue....:")
        menu_customer(username)
    elif option1== "2":
        if not ct.sefaresh_customer(username):
            print("eshtebeahi rokh dade ast")
        else:
            print("anjam shd ...")

        opt=input("press any key to continue....:")
        menu_customer(username)
    elif option1=="3":
        signin_1()
    else:
        print("dorost entekhab kon!!!!")
        menu_customer(username)


def menu_admin():
    """
    menu admin va ghabliat haee k dard
    """



    print('''
    
    1-add Foods
    2-user_orders
    3-back
    ''')
    option1=input("entekhab konid :")
    if option1== "1":
        ct.add_food_admin()
        opt=input("press any key to continue....:")
        menu_admin()
    elif option1== "2":
        ct.sabeghe_kharid_admin()

        opt=input("press any key to continue....:")
        menu_admin()
    elif option1=="3":
        signin_1()
    else:
        print("dorost entekhab kon!!!!")
        menu_admin()



    







def admin_signin():
    """
    tabe signin kardan admin ast darsorat dorostbodan etelat be menu miravad 
    
    
    """
    print("* admin gerami etelat khod ra vared namaeid ")
    username=input("username:")
    password=input("password:")
    if ct.signin_check_admin(username,password):
        menu_admin()
    else:
        print("etelat eshtebah ast dobare vared konid")
        option1=input("1-try again \n 2-back")
        if option1=="1":
            admin_signin()
        else:
            signin_1()    






def customer_signin():
    """
    tabe sign in kardan customer ast ghabeliat sakhtan acc va vorod 
    be menu ra be karbar midahad
    
    """


    option1=input("moshtari gerami ozv hastid ya kheir (yes or no) baray bargash be agha (b) /ra vared konid:").lower()
    try:
        if option1=="yes":
            username=input("username:")
            password=input("password:")
            if ct.signin_check_customer(username,password):
                menu_customer(username)
            else:
                print("etelat eshtebah ast dobare vared konid")
                customer_signin()

        elif option1=="no":
                username=input("username:")
                password=input("password:")
                
                if ct.signin(username,password):
                    menu_customer(username)
                else:
                    print("username mojod ast lotfan yek username digar entekhab konid")
                    customer_signin()

        elif option1=="b":
            signin_1()
        else : 
            raise Exception
    except Exception:
        print("vorodi eshtebah !!")
        customer_signin()

def signin_1():

    """
    tabe shore avalie va entekhab naghsh ast
    """

    option1=input("Baray vorod lotfan entekhab konid : 1-admin 2-customer baray khoroj 3 ra bezanid:")
    if option1=="1":
        admin_signin()
    elif option1=="2":
        customer_signin()

    elif option1=="3":
        exit()
    else:
        print("eshtebah vared kardi!!!")
        signin_1()
        
if __name__=="__main__":
    print('''

    Salam be Resturan ma khosh amadin !!!!xD
''')
    signin_1()