#ABA Module: Authentication Module
#Author: Vladimir Pinchuk, Dominic Santilla
#Date: Updated: April 15, 2021
#Login file is called = Login.txt

def login(userID):
    """
    Part of the code retrieved:
    https://stackoverflow.com/questions/46747524/creating-a-login-program-that-recalls-information-from-text-files
    File format: username,password,status
    Status == 1 - Logged In
    Status == 0 - Logged Out
    """
    logged_in = False
    
    with open('Login.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        
        for i in range(len(lines)):
            username, password, status = lines[i].strip().split(',')
            #Check the username against the one supplied
            if username == userID:
                #Case 4
                if (password == ""):
                    newPassword = input("This is the first time the account is being used. You must create a new password.\nPasswords may contain 1-24 upper- or lower-case letters or numbers. Choose an uncommon password that would be difficult to guess.")
                    if (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum() and (newPassword.isnumeric() or newPassword.isalpha())):
                        return ("Password is too easy to guess.")
                    elif (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum()):
                        checkNew = input("Reenter the same password: ")
                        if (checkNew == newPassword):
                            lines[i] = (userID + "," + newPassword + ",1")
                            if i < len(lines) -1:
                                lines[i] += "\n"
                            newFile =open('Login.txt', 'w')
                            newFile.writelines(lines)
                            newFile.close()
                            return ("OK (L1)")
                        else:
                            return ("Passwords do not match.")
                    else:
                        return ("Password contains illegal characters.")
                actualPass = input("Enter your password: ")
                logged_in = password == actualPass
                if logged_in:
                    if status == "1":
                        #Case 1
                        return ("An account is currently active; logout before proceeding.")
                    else:
                        #Case 3
                        lines[i] = (username + "," + password + ",1")
                        if i < len(lines) -1:
                            lines[i] += "\n"
                        newFile = open('Login.txt', 'w')
                        newFile.writelines(lines)
                        newFile.close()
                        return ("OK")
                else:
                    #Case 2
                    return ("Invalid credentials.")
    
    

def logout(userID):
    with open('Login.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        
        for i in range(len(lines)):
            username, _, status = lines[i].strip().split(',')
            if username == userID:
                if status == "1":
                    lines[i] = (username + "," + _ + ",0")
                    if i < len(lines) -1:
                        lines[i] += "\n"
                    newFile = open('Login.txt', 'w')
                    newFile.writelines(lines)
                    newFile.close()
                    return ("OK")
                else:
                    return ("No active login session.")


def changePassword(oldPW,userID):
    with open('Login.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        
        for i in range(len(lines)):
            username, password, status = lines[i].strip().split(',')
            if username == userID:
                if status == "1":
                    if oldPW == password:
                        newPassword = input("Create a new password.\nPasswords may contain 1-24 upper- or lower-case letters or numbers. Choose an uncommon password that would be difficult to guess.")
                        if (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum() and (newPassword.isnumeric() or newPassword.isalpha())):
                            return ("Password is too easy to guess.")
                        elif (len(newPassword) < 25 and len(newPassword) > 0 and newPassword.isalnum()):
                            checkNew = input("Reenter the same password: ")
                            if (checkNew == newPassword):
                                password = checkNew
                                lines[i] = (username + "," + password + ",1")
                                if i < len(lines) -1:
                                    lines[i] += "\n"
                                newFile = open('Login.txt', 'w')
                                newFile.writelines(lines)
                                newFile.close()
                                return ("OK")
                            else:
                                return ("Passwords do not match.")
                        else:
                            return ("Password contains illegal characters.")
                    else:
                        return ("Invalid credentials.")
                else:
                    return ("No active login session.")
    file.close()