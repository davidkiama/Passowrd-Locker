#!/usr/bin/env python3

from user import User
from credentials import Credentials


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user


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


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def create_credential():
    '''
    Function to create a new credential
    '''
    print("Enter your account name:")
    account = input()
    print("Would you like to use a suggested password: (y/n)")
    pwd_option = input().lower()

    if pwd_option == "y":
        password = "aqwertiuytrewq"
        print("Your password is: " + password)

    else:
        print("Enter your password:")
        password = input()

    new_credential = Credentials(account, password)
    return new_credential


def main():
    print("Welcome to Password Locker App")
    print("What is your name?")
    username = input()
    print("Enter your password:")
    password = input()
    user = create_user(username, password)
    print(f"Hello {user.username}. what would you like to do?")


if __name__ == '__main__':
    main()
