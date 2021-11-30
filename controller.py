import pickle
class query:

    def loadall(path):
        with open(path,"rb")as file :
            while True :
                    try: 
                        ok =pickle.load(file)
                    except EOFError :
                        break
                    yield ok
    

    def search(search_list,intended,):
        for item in search_list :
            if item.name == intended:
                return item
        return False

    def sigin(object,intended_name,intended_password):
        for item in object:
            if item.name == intended_name and item.password == intended_password:
                return True
        return False
