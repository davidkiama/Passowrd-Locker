class Credentials:

    credentials_list = []

    def __init__(self, account, password):
        """
        Initializes the user with a username and password
        """
        self.account = account
        self.password = password

    def save_credential(self):
        """
        Save the credential object to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        """
        Delete a credential from the credentials list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        Return the credentials list as a list
        """
        return cls.credentials_list

    @classmethod
    def find_by_account(cls, account):
        """
        Finds a credential by account and returns the credential if it exists
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
