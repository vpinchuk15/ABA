#ABA Module: Admin Actions
#Author: Dominic Santilla
#Date: Updated: April 19, 2021
#Login file is called = Login.txt

def addUser(userID):
    with open('Login.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        if(len(userID) == 0 or len(userID) > 16 or userID.isalnum() == False):
            return ("Invalid userID")
        for line in lines:
            check = line.split(",")
            if check[0] == userID:
                return "Account already exists"
        lines[-1] +="\n"
        lines.append(userID + ",,0")
        newFile = open('Login.txt', 'w')
        newFile.writelines(lines)
        newFile.close()
        return ("OK")

def deleteUser(userID):
    with open('Login.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        if(len(userID) == 0 or len(userID) > 16 or userID.isalnum() == False):
            return ("Invalid userID")
        found = False
        for i in range(len(lines)):
            if found == False:
                check = lines[i].split(",")
                if check[0] == userID:
                    found = True
            if found == True:
                if(i == len(lines)-1):
                    lines.pop(-1)
                else:
                    lines[i] = lines[i+1]
        if(found == True):
            newFile = open('Login.txt', 'w')
            for i in range(len(lines)):
                if i == len(lines) -1 :
                    lines[i] = lines[i].strip()    
                newFile.write(lines[i])
            newFile.close()
            return ("OK")
        else:
            return ("Account does not exist")
        