class Credentials:

    credentials_list = []

    def __init__(self, account, password):
        self.account = account
        self.password = password

    def save_credential(self):
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def find_by_account(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
