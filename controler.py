from model import Users

def register(username, password):
    if Users.query.exist("username", username):
        raise Exception("hamchin useri darim!")
    user = Users(username, password)
    user.save()

    return "be khubi va khoshi ezafe shod"