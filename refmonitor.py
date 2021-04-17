#ABA Module: Reference Monitor
#Author: Dominic Santilla
#Date: Updated: April 16, 2021

def Session():
    global userID = None
    command = None
    parameter = None
    version = 0.1
    
    print("Address Book Application, version "+ str(version) + ". Type “HLP” for a list of commands.")
    while(True):
        command_str = input("Enter Command>")
        field_list = []
        try:
            command_str.encode('utf-8')
            command = command_str[:3]
            if(len(command_str) > 3):
                for i in range(3,len(command_str)):
                    pass                                ### NOT IMPLEMENTED YET

            if(command == "EXT"):
                exit()
            elif(command == "LIN"):
                if(userID == None):
                    userID = parameter
                else:
                    print("Already logged in. Must log out to log into a different account.")
                    continue
            elif(command == "LOU"):
                userID = None
            processCommand(command, parameter, userID)
        except UnicodeDecodeError:
            print("This string contains more than just the ASCII characters.")

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

def getUserID():
    return userID

