#ABA Module: Login
#Authors: Nathan Shah
#Date: Updated: April 17, 2021

import pickle
import bcrypt
from cryptography.fernet import Fernet #noqa

class Login:
    """
    Models the user database.
    """
    def __init__(self):
        self.table = {}
        
        self.table['admin'] = None

        try:
            open('loginFile.txt', 'x')
            self.key = Fernet(Fernet.generate_key())
            self.saveTable(self.table)

        except FileExistsError:
            return None

    def openTable(self):
        """
        Opens the loginFile.txt
        """
        # opening the encrypted file
        with open('loginFile.txt', 'rb') as enc_file:
            encrypted = enc_file.read()
  
        # decrypting the file
        decrypted = self.key.decrypt(encrypted)
  
        # opening the file in write mode and
        # writing the decrypted data
        with open('loginFile.txt', 'wb') as dec_file:
            dec_file.write(decrypted)

        with open("loginFile.txt", "rb") as f:
            table = pickle.load(f)
            f.close()
        
        return table

    def saveTable(self,table):
        with open("loginFile.txt", "wb") as f:
            pickle.dump(table,f)
        
        f.close()

        with open('loginFile.txt', 'rb') as file:
            original = file.read()
        
        # encrypting the file
        encrypted = self.key.encrypt(original)
    
        # opening the file in write mode and 
        # writing the encrypted data
        with open('loginFile.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        return None

def login(Login,userID):
    """
    Logins a user
    """
    table = Login.openTable()

    if userID not in table:
        print("Invalid Credentials")
        return False,''

    if table[userID] == None:
        print("This is the first time the account is being used.")
        print("You must create a new password. Passwords may contain 1-24 upper- or lower-case letters or numbers.")
        print("Choose an uncommon password that would be difficult to guess.")

        password = input("Enter Password:")
        password1 = input("Renter Password:")

        if password != password1:
            print("Passwords do not match.")
            return False, 'LF'

        
        if not password.isascii() and password.isalnum() or len(password) > 24 or len(password) < 1 :
            print("Password contains illegal characters.")
            return False, 'FPC'

        if  password.isalpha() or password.isdigit():
            print("Password is too easy to guess.")
            return False, 'FPC'

        table[userID] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        Login.saveTable(table)

        return True, 'LS, L1'

    else:
        password = input("Enter password:")
        
        if bcrypt.checkpw(password.encode("utf-8"), table[userID]):
            print("OK")
            return True, 'LS'
        else:
            return False, 'LF'

def addUser(Login,userID):
    """
    Admin only - add user
    """
    table = Login.openTable()

    if len(userID) > 16:
        print("Invalid UserID")
        return False, ''

    if len(table) == 8:
        print("Too many accounts.")
        return False, ''

    if userID in table:
        print("Account already exists")
        return False, ''
    
    table[userID] = None

    Login.saveTable(table)

    return True, 'AD'

def deleteUser(Login,userID):
    """
    Admin only - delete user
    """
    table = Login.openTable()

    if len(userID) > 16:
        print("Invalid UserID")
        return False, ''

    if userID not in table:
        print("Account does not exists")
        return False, ''

    table.pop(userID)

    Login.saveTable(table)

    print("OK")
    return True, 'DA'


def changePassword(Login, userID, oldPassword):
    """
    Changes Password
    """
    table = Login.openTable()

    if bcrypt.checkpw(oldPassword.encode("utf-8"), table[userID]):

        print("Create a new password. Passwords may contain up to 24")
        print("upper- or lower-case letters or numbers. Choose an")
        print("uncommon password that would be difficult to guess.")
        
        password = input("Enter New Password:")
        password1 = input("Renter New Password:")

        if password != password1:
            print("Passwords do not match.")
            return False, 'FPC'
        
        if not password.isascii() and password.isalnum() or len(password) > 24 or len(password) < 1:
            print("Password contains illegal characters.")
            return False, 'FPC'

        if  password.isalpha() or password.isdigit():
            print("Password is too easy to guess.")
            return False, 'FPC'

        table[userID] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        Login.saveTable(table)
        print("OK")
        return True, 'SPC'

    else:
        Login.saveTable(table)
        print("Invalid Credentials.")

        if table.get(userID, None) != None:
            return False, 'FPC'
        else:
            return False, ''
    
def listUsers(Login):
    """
    Lists the users 
    """
    table = Login.openTable()
    Login.saveTable(table)

    for user in table:
        print(user)

    print("OK")
    return None

def checkStartup(Login):
    """
    Checks if the first startup
    """

    table = Login.openTable()
    Login.saveTable(table)

    if table['admin'] != None:
        return True
    
    return False

