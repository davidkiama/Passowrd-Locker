#!/usr/bin/env python3

from user import User
from credentials import Credentials


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


def check_password(password):
    return User.check_password(password)


def ask_password():
    print("Enter User password:")
    password = input()
    return password


def create_credential(account, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(account, password)
    return new_credential


def save_credential(credential):
    '''
    Function to create a new credential
    '''
    credential.save_credential()


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def find_credential(account):
    '''
    Function that finds a credential by account and returns the credential
    '''
    return Credentials.find_by_account(account)


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def main():
    print("Welcome to Password Locker App")
    print("What is your name?")
    username = input()
    print("Enter your password:")
    password = input()
    user = create_user(username, password)
    print(f"Hello {user.username}. what would you like to do?")
    print('\n')

    while True:
        print("""Use these short codes : 
        sc - Store existing credentials,
        dc - Display credentials,
        cc - Create a new credential,
        del- delete a credential, 
        exit -exit the contact list """)

        short_code = input().lower()

        if short_code == "sc":
            print("Enter your account name:")
            account = input()
            print("Enter your password:")
            password = input()
            save_credential(create_credential(account, password))
            print('\n')

        elif short_code == "cc":
            print("Enter your account name:")
            account = input()
            print("Would you like to use a suggested password: (y/n)")
            pwd_option = input().lower()

            if pwd_option == "y":
                password = "aqwertiuytrewq"
                print("Your password is: " + password)

            else:
                print("Enter your preferred password:")
                password = input()
            save_credential(create_credential(account, password))
            print('\n')

        elif short_code == "dc":

            user_password = ask_password()
            if user.check_password(user_password):

                if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for credential in display_credentials():
                        print(f"{credential.account} {credential.password}")

                    print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == "del":
            user_password = ask_password()
            if user.check_password(user_password):
                print("Enter the account name you want to delete:")
                account = input()
                if find_credential(account):
                    delete_credential(find_credential(account))
                    print("Credential has been deleted")
                    print('\n')
                else:
                    print("That credential does not exist")
                    print('\n')

        elif short_code == "exit":
            print("Logging out .......")
            break
        else:
            print("Please use the short codes provided")


if __name__ == '__main__':
    main()
