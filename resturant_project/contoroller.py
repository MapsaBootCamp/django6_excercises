from models import Admin,Customer,Foods
from db import BaseQuery
import setting
from datetime import datetime
def signin(username:str,password:str):
    if Customer.db_obj.exist("username",username):
        return False
    else:
        e=Customer(username,password)
        e.save()
        return True
def signin_check_customer(username,password):
    return Customer.db_obj.signin_check(username,password)
def signin_check_admin(username,password):
    return Admin.db_obj.signin_check(username,password)    



def sabeghe_kharid_customer(username):
    with open(setting.Gozaresh_Dir/"gozaresh.txt","r") as file:
        for i in file.readlines():
            history=i.split(":")
            for i in range(0,len(history),2):
                if history[i]==username:
                    print(history[i+1])

def sefaresh_customer(username):
    i=1
    for elm in Foods.db_obj.loadall():
        print (f"{i}-{elm.__dict__}")
        i+=1
    option1=input("please select all you want to have with space char with:").split(" ")
    choises=list(map(int,option1))
    option2=input("chand adad? ba space vared konid" ).split(" ")
    tedad=list(map(int,option2))
    i,flage,name=0,False,"name"
    for elm in Foods.db_obj.loadall():
        for clm in choises:
            if i==clm-1:
                if getattr(elm,"activate") !="yes":
                    print(f"{getattr(elm,name)} ghable sefaresh nist")
                    flage=True
                else:
                    date=datetime.now().strftime("%Y %B %d ")
                    time=datetime.now().strftime("%X")
                    with open(setting.Gozaresh_Dir/"gozaresh.txt","a") as file:
                        file.write(f"{username}:{elm.name} be tedad {tedad[i]} dar tarikh {date} va saat {time} kharidari kard.\n")
                        flage=True
                        
        i+=1
    if flage:
        return True
    else:
        return False
def sabeghe_kharid_admin():
    with open(setting.Gozaresh_Dir/"gozaresh.txt","r") as file:
        print(file.read())



def add_food_admin():
    name=input("esm ghaze:")
    price=input("gheimat:")
    mojodi=input("ghaza mojod ast ya khier (yes or no ):")
    inf=input("etelat marbot be ghaza:")

    obj1=Foods(name,price,mojodi,inf)
    obj1.save()
    print("ba movafaghiat sabt shod ")