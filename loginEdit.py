#ABA Module: Login
#Authors: Nathan Shah
#Date: Updated: April 17, 2021

import pickle
import bcrypt


class Login:
    """
    Models the user database.
    """
    def __init__(self):
        self.table = {}
        
        self.table['admin'] = None

        try:
            open("loginFile.txt", "x")
            with open("loginFile.txt", "wb") as f:
                pickle.dump(self.table, f)

            f.close()
        except FileExistsError:
            return None

def login(userID):
    """
    Logins a user
    """
    table = openTable()

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
        
        if not password.isascii():
            print("Password contains illegal characters.")
            return False, 'LF'

        if password.isalpha() or password.isdigit() or password.isalnum():
            print("Password is too easy to guess.")
            return False, 'LF'

        table[userID] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        saveTable(table)

        return True, 'LS, L1'

    else:
        password = input("Enter password:")
        
        if bcrypt.checkpw(password.encode("utf-8"), table[userID]):
            print("OK")
            return True, 'LS'
        else:
            return False, 'LF'

def addUser(userID):
    """
    Admin only - add user
    """
    table = openTable()

    if len(userID) > 64:
        print("Invalid UserID")
        return False, ''

    if len(table) > 8:
        print("Too many accounts.")
        return False, ''

    if table.get(userID, None) != None:
        print("Account already exists")
        return False, ''
    
    table[userID] = None

    saveTable(table)

    return True, 'AD'

def deleteUser(userID):
    """
    Admin only - delete user
    """
    table = openTable()

    if len(userID) > 64:
        print("Invalid UserID")
        return False, ''

    if table.get(userID, None) == None:
        print("Account does not exists")
        return False, ''

    table.pop(userID)

    saveTable(table)

    print("OK")
    return True, 'DA'


def changePassword(userID):
    """
    Changes Password
    """
    table = openTable()

    oldPassword = input("Enter old password:")
    
    if bcrypt.checkpw(oldPassword.encode("utf-8"), table[userID]):
        
        password = input("Enter New Password:")
        password1 = input("Renter New Password:")

        if password != password1:
            print("Passwords do not match.")
            return False, 'FPC'
        
        if not password.isascii() and password.isalnum():
            print("Password contains illegal characters.")
            return False, 'FPC'

        if  password.isalpha() or password.isdigit():
            print("Password is too easy to guess.")
            return False, 'FPC'

        table[userID] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        saveTable(table)
        print("OK")
        return True, 'SPC'

    else:
        print("Invalid Credentials.")

        if table.get(userID, None) != None:
            return False, 'FPC'
        else:
            return False, ''
    
def listUsers():
    """
    Lists the users 
    """
    table = openTable()

    for user in table:
        print(user)

    print("OK")
    return None

def openTable():
    """
    Opens the databaseFile.txt
    """
    with open("loginFile.txt", "rb") as f:
        table = pickle.load(f)
        f.close()
    
    return table

def saveTable(table):
    with open("loginFile.txt", "wb") as f:
        pickle.dump(table,f)
    
    f.close()

    return None

def checkStartup():
    """
    Checks if the first startup
    """

    table = openTable()

    if table['admin'] != None:
        return True
    
    return False

