class User:

    def __init__(self, username, password):
        """
        Initializes the user with a username and password
        """

        self.username = username
        self.password = password

    def check_password(self, password):
        """
        Checks if the password entered if the same 
        as the one used when creating the user
        """
        if self.password == password:
            return True
        else:
            print("Wrong password")
            return False
