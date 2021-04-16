#ABA Module: Authentication Module
#Author: Vladimir Pinchuk
#Date: Updated: April 15, 2021
#Login file is called = Login.txt

def login(actualUser,actualPass):
    """
    Code retrieved:
    https://stackoverflow.com/questions/46747524/creating-a-login-program-that-recalls-information-from-text-files
    """
    logged_in = False
    with open('Login.txt', 'r') as file:
        for line in file:
            username, password = line.split(',')
            # Check the username against the one supplied
            if username == actualUser:
                logged_in = password == actualPass
                break

    if logged_in:
        return True
    else:
        return False

def logout():
    #TODO: Logout and possibly save in logs?
    pass

def changePassword():
    #TODO: Change password in database?
    pass
