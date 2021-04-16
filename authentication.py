#ABA Module: Authentication Module
#Author: Vladimir Pinchuk
#Date: Updated: April 15, 2021
#Login file is called = Login.txt

def login(actualUser):
    """
    Part of the code retrieved:
    https://stackoverflow.com/questions/46747524/creating-a-login-program-that-recalls-information-from-text-files
    File format: username,password,status
    Status == 1 - Logged In
    Status == 0 - Logged Out
    """
    logged_in = False
    
    with open('Login.txt', 'w+') as file:
        for line in file:
            username, password, status = line.split(',')
            #Check the username against the one supplied
            if username == actualUser:
                #Case 4
                if (actualPass == ""):
                    newPassword = input("This is the first time the account is being used. You must create a new password.\nPasswords may contain 1-24 upper- or lower-case letters or numbers. Choose an uncommon password that would be difficult to guess.")
                    if (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum() and (newPassword.isnumeric() or newPassword.isalpha())):
                        return ("Password is too easy to guess")
                    elif (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum()):
                        checkNew = input("Reenter the same password: ")
                        if (checkNew == newPassword):
                            file.write(actualUser + "," + newPassword + ",1" +'\n')
                            return ("Ok")
                        else:
                            return ("Passwords do not match")
                    else:
                        return ("Password contains illegal characters")
                actualPass = input("Enter your password: ")
                logged_in = password == actualPass
                if logged_in:
                    if status == "1":
                        #Case 1
                        return ("An account is currently active; logout before proceeding.")
                    else:
                        #Case 3
                        return True
                else:
                    #Case 2
                    return ("Invalid credentials.")

def logout():
    #TODO: Logout and possibly save in logs? Put 0 status
    pass

def changePassword():
    #TODO: Change password in database?
    pass
