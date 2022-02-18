class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        if self.password == password:
            return True
        else:
            print("Wrong password")
            return False
