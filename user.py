class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def check_password(cls, password):
        if cls.password == password:
            return True
        else:
            print("Wrong password")
            return False
