import bcrypt
import pickle

class BaseQuery:


    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def loadall(self):
        with open(self.file_path, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    

    def exist(self, query_params, query_value) -> bool:
        for elm in self.loadall():
            if getattr(elm, query_params) == query_value:
                return True
        return False


    def signin_check(self,username,password):
        flage=False
        for elm in self.loadall():
            if  elm.username == username and bcrypt.checkpw(password, elm.password) :
                flage=True
            
        if flage :
            return True
        else:
            return False

