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
                print("Need to login to access other commands.")
        
        else:
            continue
            #we are logged in access to differnt commands oka

def processCommand(command, parameter, userID):
    good = "OK"         #REPLACE AFTER IMPLEMENTING FUNCTIONS
    bad = "Invalid"     #REPLACE AFTER IMPLEMENTING FUNCTIONS
    

    if userID == None:
        if(command == "LIN"):
            #login(parameter)
            return good
        else:
            print("Must log in first.")
            return bad        
    else:
        if(command == "LOUT"):
            #logout()
            return good
        elif (command == "CHP"):
            #changePassword(parameter)
            return good
        elif(command in ["ADU", "DEU", "DAL"]): #Admin-Only Commands
            if(userID == "admin"):
                if (command == "ADU"):
                    #addUser(parameter)
                    pass
                elif (command == "DEU"):
                    #deleteUser(parameter)
                    pass
                elif (command == "DAL"):
                    #displayAuditLog(parameter)
                    pass
                return good
            else:
                print("Unauthorized to access admin commands")
                return bad    
        elif (command == "ADR"):
            #addRecord(parameter)
            return good
        elif (command == "Delete Record"):
            #deleteRecord()
            return good
        elif (command == "Get Record"):
            #getRecord()
            return good
        elif (command == "Import database"):
            #importDatabase()
            return good
        elif (command == "Export database"):
            #exportDatabase
            return good
        elif (command == "Help"):
            #display commands
            return good
        else:
            print("Invalid Command. Type \"HLP\" for a list of valid commands and their syntax \nor type \"Help [<command name>]\" for the command syntax of a specific command.")

if __name__ == "__main__":
    runSession()

