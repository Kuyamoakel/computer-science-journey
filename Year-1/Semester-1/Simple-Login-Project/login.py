# importing 2 module
# 1. json for file handling
# 2. os for refreshing the window terminal for cleaner terminal
import json
import os

class Account_Manager:
    def __init__(self):
        self.account = []
        self.FILE_ACCOUNT = "account.json"
        self.run = True

    def load_account(self): # load account this load the data from json file
        try:
            with open(self.FILE_ACCOUNT, "r") as f:
                self.account = json.load(f)
        except FileNotFoundError:
            print("ACCOUNT DOESN'T EXIT")

    def save_account(self): # save account and put it in the json file
        with open(self.FILE_ACCOUNT, "w") as f:
            json.dump(self.account, f, indent=4)

    def clear_screen(self): # this is the os module reset and refresh the terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def create_account(self): # function for creating a account
        self.clear_screen()
        print("OKAY! PUT A VALID USERNAME AND PASSWORD")
        username = input("USERNAME: ").lower()
        password = input("PASSWORD: ")

        self.account.append ({ #append or add the username and password that the user will input
            "username": username, 
            "password": password
        })
        self.save_account()# will save the data straight to json file

    def login_account(self): # function resposible for login account
        self.clear_screen() # everytime na papasok sa function nato mag rerefresh yung terminal
        print("LET'S LOGIN")
        user_input = input("USERNAME: ").lower()
        pass_input = input("PASSWORD: ")

        for acc in self.account: # for loop para ma access yung list of dictionaries na account
            if user_input == acc['username'] and pass_input  == acc['password']: # ternary operator
                print("WELCOME TO YOUR ACCOUNT!")
                self.run = False # when the account is right, the program will return false to run to stop the loop
                return
        print("Sorry, please try again")# error handling

    def start(self):
        self.load_account() # for loading the data
        while self.run: # while loop na sa run na variable na naka boolean
            print("\n~~~~~~~~~ WELCOME TO FACEBOOK ~~~~~~~~~")
            print("[1] LOGIN \n[2] CREATE AN ACCOUNT")
            login = input("CHOOSE ONE: ")

            if login == "1": #goes to function login_account()
                self.login_account()
            elif login == "2": #goes to function create_account()
                self.create_account()
            else:
                print("INVALID INPUT")

if __name__ == "__main__":
    account_manager = Account_Manager()
    account_manager.start()
    