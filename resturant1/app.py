from controller import register,login

print("""
            SALAM..... Be Restorane Saman Khosh Amadid
""")


question = input('username darid?(y/n) :')
# try:
if question == 'n':
    print('register now')
    register('username', 'password')

elif question == 'y':
    login('username', 'password')
        
            
# except:
#     print('tekrari e user')