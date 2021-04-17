#ABA Module: HUB
#Author: Nathan Shah
#Date: Updated: April 16, 2021

import datacom

class Session:

    def __init__(self):
        self.username = None
        self.access = None

def runSession():

    print("Address Book Application, version "+ '0.1' + ". Type “HLP” for a list of commands.")
    session = Session()

    datacom.UserDatabase()
    #create oter classes for the other modules

    while(True):
        command_str = input("Enter Command>")

        command = command_str[:3]

        if session.username == None:
            if command == 'EXT':
                exit()
            
            if command == "LIN":
                if session.username != None:
                    print("Already logged in.")
                else:
                    continue
                #send to login
                #if good then change seesion.usernme = username
                #session.access = 1 (User Level) if 2 (admin level)

            if command == "HLP":
                print("Add help stuff here")
            else:
                print("Need to login to access other commands or command is not valid.")
        
        elif session.access == 2:
            if command == "ADU":
                continue
            if command == "DEU":
                continue
            if command == "DAL":
                continue
            if command == "LOUT":
                continue
        else:
            if command == "ADR":
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

