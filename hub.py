#ABA Module: HUB
#Authors: Dominic Santilla, Nathan Shah
#Date: Updated: April 17, 2021

import datacom
import authentication

class Session:

    def __init__(self):
        self.username = 'Hello'
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

        command = command_str[:3]
        fieldValues = command_str[3:]
        
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
                fv = parse(fieldValues)
                datacom.addRecord(session.getUsername(), fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                   fv[9], fv[10], fv[11] )
                continue
            elif command == "DER":
                fv = parse2(fieldValues)
                datacom.deleteRecord(session.getUsername(),fv)
                continue
            elif command == "EDR":
                fv = parse(fieldValues)
                datacom.editRecord(session.getUsername(), fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                    fv[9], fv[10], fv[11] )
                continue
            elif command == "RER":
                fv = parse3(fieldValues)
                datacom.readRecord(session.getUsername(), fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                   fv[9], fv[10], fv[11] )
                continue
            elif command == "IMD":
                fv = parse2(fieldValues)
                datacom.importDatabase(session.getUsername(), fv)
                continue
            elif command == "EXD":
                fv = parse2(fieldValues)
                datacom.exportDatabase(session.getUsername(),fv)
                continue
            elif command == 'EXT':
                exit()
            else:
                print("Command is not valid.")

def parse(fieldValues):
    """
    Creates values for entry into ADR, EDR
    """
    cleaned = ['']*12

    if len(fieldValues) == 0:
        return cleaned
    else:
        output = [s for s in fieldValues.split('"') if s.strip() != '']
        cleaned[0] = output[0].strip()

    for i in range(1,len(output),2):
        if output[i] == 'SN=':
            cleaned[1] = output[i+1]
        elif output[i] == 'GN=':
            cleaned[2] = output[i+1]
        elif output[i] == 'PEM=':
            cleaned[3] = output[i+1]
        elif output[i] == 'WEM=':
            cleaned[4] = output[i+1]
        elif output[i] == 'PPH=':
            cleaned[5] = output[i+1]
        elif output[i] == 'WPH=':
            cleaned[6] = output[i+1]
        elif output[i] == 'SA=':
            cleaned[7] = output[i+1]
        elif output[i] == 'CITY=':
            cleaned[8] = output[i+1]
        elif output[i] == 'STP=':
            cleaned[9] = output[i+1]
        elif output[i] == 'CTY=':
            cleaned[10] = output[i+1]
        elif output[i] == 'PC=':
            cleaned[11] = output[i+1]
        else:
            continue
    
    return cleaned

def parse2(fieldValues):
    output = fieldValues.split()

    return output[0]

def parse3(fieldValues):

    cleaned = [None]*12

    if len(fieldValues) == 0:
        return cleaned
    else:
        output = [s for s in fieldValues.split()]
        cleaned[0] = output[0].lstrip()

    for i in range(1,len(output),2):
        if output[i] == 'SN':
            cleaned[1] = output[i]
        elif output[i] == 'GN':
            cleaned[2] = output[i]
        elif output[i] == 'PEM':
            cleaned[3] = output[i]
        elif output[i] == 'WEM':
            cleaned[4] = output[i]
        elif output[i] == 'PPH':
            cleaned[5] = output[i]
        elif output[i] == 'WPH':
            cleaned[6] = output[i]
        elif output[i] == 'SA':
            cleaned[7] = output[i]
        elif output[i] == 'CITY':
            cleaned[8] = output[i]
        elif output[i] == 'STP':
            cleaned[9] = output[i]
        elif output[i] == 'CTY':
            cleaned[10] = output[i]
        elif output[i] == 'PC':
            cleaned[11] = output[i]
        else:
            continue

    return cleaned

if __name__ == "__main__":
    runSession()

