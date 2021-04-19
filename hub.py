#ABA Module: HUB
#Authors: Dominic Santilla, Nathan Shah
#Date: Updated: April 17, 2021

import datacom
import authentication
import auditLog
import adminActions

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

    print("Address Book Application, version "+ '0.5' + ". Type “HLP” for a list of commands.")
    session = Session()

    datacom.UserDatabase()
    auditLog.AuditLog()
    #create oter classes for the other modules
    if(authentication.checkStartup() == True):
        print("First Time Startup. Create password for admin account.")
        exit_code = authentication.login("admin")
        if(exit_code == "OK (L1)"):
            session.setUsername("admin")
            session.setAccess(2)
            auditLog.addLog("L1", session.getUsername())
            auditLog.addLog("LS", session.getUsername())
            print("OK")
    while(True):
        command_str = input("Enter Command>")

        command = command_str[:3]

        fieldValues = command_str[4:]
        
        exit_code = None
        if command == 'EXT':
                print("OK")
                if(session.getUsername != None):
                    authentication.logout(session.getUsername())
                exit()
        elif command == "HLP":
            print(showHelp(fieldValues))
        elif session.getUsername() == None:  
            if command == "LIN":
                exit_code = authentication.login(fieldValues)
                if(exit_code == "OK" or exit_code == "OK (L1)"):
                    session.setUsername(fieldValues)
                    if(session.getUsername() == "admin"):
                        session.setAccess(2)
                    else:
                        session.setAccess(1)
                    if(exit_code == "OK (L1)"):
                        auditLog.addLog("L1", session.getUsername())
                    auditLog.addLog("LS", session.getUsername())
                    print("OK")
                else:
                    auditLog.addLog("LF", fieldValues)
                    print(exit_code)
                #send to login
                #if good then change seesion.usernme = username
                #session.access = 1 (User Level) if 2 (admin level)
            else:
                print("No Active Login Session.")
        elif command == "LIN":
            print("Already logged in.")
        elif command == "LOU":
            exit_code = authentication.logout(session.getUsername())
            if(exit_code == "OK"):
                session.setUsername(None)
                session.setAccess(0)
            print(exit_code)
        elif command == "CHP":
            exit_code = authentication.changePassword(fieldValues, session.getUsername())
            if(exit_code == "OK"):
                auditLog.addLog("SPC", session.getUsername())
            else:
                auditLog.addLog("FPC", session.getUsername())
            print(exit_code)
            
        elif session.getAccess() == 2:
            if command == "ADU":
                exit_code = adminActions.addUser(fieldValues)
                print(exit_code)
                if exit_code == "OK":
                    auditLog.addLog("AU", session.getUsername())
            elif command == "DEU":
                exit_code = adminActions.deleteUser(fieldValues)
                print(exit_code)
                if exit_code == "OK":
                    auditLog.addLog("DU", session.getUsername())
            elif command == "DAL":
                if(len(fieldValues) > 0):
                    auditLog.displayLog(fieldValues)
                else:
                    auditLog.displayLog()
            elif command in ["ADR", "DER", "EDR", "RER", "IMD", "EXD"]:
                print("Admin not authorized")
            else:
                print("Command is not valid.")
        else:
            if command in ["ADU", "DEU", "DAL"]:
                print("Admin not active")
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

def showHelp(command):
    if(command == "" or command == "LIN"):
        print("LIN <userID>")
    if(command == "" or command == "LOU"):
        print("LOU")
    if(command == "" or command == "CHP"):
        print("CHP <old password>")
    if(command == "" or command == "ADU"):
        print("ADU <userID>")
    if(command == "" or command == "DEU"):
        print("DEU <userID>")
    if(command == "" or command == "DAL"):
        print("DAL [<userID>]")
    if(command == "" or command == "ADR"):
        print("ADR <recordID> [<field1=value1> <field2=value2> ...]")
    if(command == "" or command == "DER"):
        print("DER <recordID>")
    if(command == "" or command == "EDR"):
        print("EDR <recordID> <field1=value1> [<field2=value2> ...]")
    if(command == "" or command == "RER"):
        print("RER [<recordID>] [<fieldname> ...]")
    if(command == "" or command == "IMD"):
        print("IMD <Input_File>")
    if(command == "" or command == "EXD"):
        print("EXD <Output_file>")
    if(command == "" or command == "HLP"):
        print("HLP [<command name>]")
    if(command == "" or command == "EXT"):
        print("EXT")
    return "OK"
if __name__ == "__main__":
    runSession()

