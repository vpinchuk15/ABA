#ABA Module: HUB
#Authors: Dominic Santilla, Nathan Shah
#Date: Updated: April 17, 2021

import datacom
import authentication

class Session:

    def __init__(self):
        self.username = None
        self.access = 0

    def getUsername(self):
        return self.username

    def getAccess(self):
        return self.access

    def setUsername(self, userID):
        self.username = userID
    
    def setAccess(self, access_level):
        self.access = access_level

def runSession():

    print("Address Book Application, version "+ '0.1' + ". Type “HLP” for a list of commands.")
    session = Session()

    datacom.UserDatabase()
    #create oter classes for the other modules

    while(True):
        command_str = input("Enter Command>")

        command_str.split(";")
        command = command_str[0]
        exit_code = None
        if session.username == None:
            if command == 'EXT':
                exit()
            
            if command == "LIN":
                if session.getUsername() != None:
                    print("Already logged in.")
                else:
                    exit_code = authentication.login(command_str[1])
                    if(exit_code == 'Ok.'):
                        session.setUsername(command_str[1])
                        if(session.getUsername() == "admin"):
                            session.setAccess = 2
                        else:
                            session.setAccess = 1
                    else:
                        print(exit_code)
                #send to login
                #if good then change seesion.usernme = username
                #session.access = 1 (User Level) if 2 (admin level)

            if command == "HLP":
                print("Add help stuff here")
            else:
                print("Need to login to access other commands or command is not valid.")
        
        elif command == "LOU":
            exit_code = authentication.logout(session.getUsername())
            if(exit_code == "Ok"):
                session.setUsername(None)
                session.setAccess(0)
            else:
                print(exit_code)
        elif command == "CHP":

            exit_code = authentication.changePassword(command_str[2], session.getUsername())
            if(exit_code != "Ok."):
                print(exit_code)
        elif session.access == 2:
            if command == "ADU":
                continue
            if command == "DEU":
                continue
            if command == "DAL":
                continue
        else:
            if command == "ADR":
                #difficulty parsing command line and sending as parameters. Maybe simply send all tokens and parse within AddRecord function?
                continue
            elif command == "DER":
                continue
            elif command == "EDR":
                continue
            elif command == "RER":
                continue
            elif command == "IMD":
                continue
            elif command == "EXD":
                continue
            else:
                print("Command is not valid.")


if __name__ == "__main__":
    runSession()

