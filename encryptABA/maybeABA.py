#ABA Module: HUB
#Authors: Dominic Santilla, Nathan Shah
#Date: Updated: April 17, 2021

import maybe as datacom
import maybeLogin as login
import maybeA as auditLog

class InvalidInput(Exception): pass

class Session:

    def __init__(self):
        self.username = None
        self.access = 0

def runSession():

    print("Address Book Application, version "+ '0.1' + ". Type “HLP” for a list of commands.")
    
    session = Session()

    d = datacom.UserDatabase()
    a = auditLog.AuditLog()
    l = login.Login()
    
    while True:
        if login.checkStartup(l):
            break
        else:
            print("First Time Startup. Create password for admin account.")
            code,audit = login.login(l,'admin')

            if code:
                session.username = 'admin'
                session.access = 1
                auditLog.addLog(a,audit,session.username)
                break
            else:
                print("Try again. This is a necessay condition")

    while True:
        print()
        command_str = input("Enter Command>")

        command = command_str[:3]

        fieldValues = command_str[3:].strip()
        
        if command == 'EXT':
            session.username = None
            session.access = 0
            print("OK")
            exit()
        elif command == "HLP":
            print(showHelp(fieldValues))
        elif session.username == None:  
            
            if command == "LIN":
                if len(fieldValues) == 0:
                    print("No userID given.")
                    continue

                code,audit = login.login(l,fieldValues)

                if code:
                    session.username = fieldValues
                    auditLog.addLog(a,audit,session.username)

                    if session.username == 'admin':
                        session.access = 1
                    else:
                        session.access = 0

                else:
                    if audit != '':
                        auditLog.addLog(a,audit,fieldValues)
                        print("Invalid Credentials")

            else:
                print("No active login session.")

        elif command == "LIN":
            print("An account is currently active; logout before proceeding.")

        elif command == "LOU":

            auditLog.addLog(a,'LO', session.username)
            session.username = None
            session.access = 0
            print("OK")
            
        elif command == "CHP":

            if len(fieldValues) == 0:
                print("Old password not given.")
                continue

            code,audit = login.changePassword(l,session.username,fieldValues)

            if code:
                auditLog.addLog(a,audit,session.username)

            else:
                if audit != '':
                    auditLog.addLog(a,audit,fieldValues)

            
        elif session.access == 1:
            if command in ["ADR", "DER", "EDR", "RER", "IMD", "EXD"]:
                print("Admin not authorized")
                
            elif command == "ADU":
                login.addUser(l,fieldValues)
                auditLog.addLog(a,"AU", 'admin')

            elif command == "DEU":
                login.deleteUser(l,fieldValues)
                auditLog.addLog(a,"DU", 'admin')

            elif command == "DAL":
                if(len(fieldValues) > 0):
                    auditLog.displayLog(a,fieldValues)
                else:
                    auditLog.displayLog(a)

            elif command == "LSU":
                login.listUsers(l)
            
            else:
                print("Command is not valid.")
        
        else:
            if command in ["ADU", "DEU", "DAL"]:
                print("Admin not active")

            elif command == "ADR":
                try:
                    fv = parse(fieldValues)
                    datacom.addRecord(d,session.username, fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                    fv[9], fv[10], fv[11] )
                except InvalidInput:
                    print("One or more fields are incorrect")
                
                continue

            elif command == "DER":
                fv = parse2(fieldValues)
                datacom.deleteRecord(d,session.username,fv)
                continue

            elif command == "EDR":
                try:
                    fv = parse(fieldValues)
                    datacom.editRecord(d,session.username, fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                        fv[9], fv[10], fv[11] )
                except InvalidInput:
                    print("One or more fields are incorrect.")
                
                continue

            elif command == "RER":
                fv = parse3(fieldValues)
                datacom.readRecord(d,session.username, fv[0], fv[1], fv[2], fv[3], fv[4], fv[5], fv[6], fv[7], fv[8],
                                   fv[9], fv[10], fv[11] )
                continue

            elif command == "IMD":
                fv = parse2(fieldValues)
                datacom.importDatabase(d,session.username, fv)
                continue

            elif command == "EXD":
                try:
                    fv = parse2(fieldValues)
                    datacom.exportDatabase(d,session.username,fv)
                except:
                    print("No data to export.")
                continue
            else:
                print("Unrecognized command.")

def parse(fieldValues):
    """
    Creates values for entry into ADR, EDR
    """
    cleaned = [None]*12

    if len(fieldValues) == 0:
        return cleaned
    else:
        outputA = [s for s in fieldValues.split('"') if s.strip() != '']

        output = []
        if len(outputA) > 1:
            outputB = outputA[0].split()
            output.append(outputB[0])
            output.append(outputB[1])

            for i in range(2,len(outputA)+1):
                output.append(outputA[i-1].strip())
            cleaned[0] = output[0]
        else:
            cleaned[0] = outputA[0]
        
        
        for i in range(1,len(output),2):
                if i not in ['SN=', 'GN=', 'PEM=', 'WEM=', 'PPH=', 'WPH=', 'SA=', 'CITY=', 'STP=', 'CTY=', 'PC=']:
                    raise InvalidInput
                else:
                    continue

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

    if len(fieldValues) > 0:
        output = fieldValues.split()

        return output[0]
    else:
        return ''

def parse3(fieldValues):

    cleaned = [None]*12

    if len(fieldValues) == 0:
        cleaned[0] = ''
        return cleaned

    else:
        outputA = [s for s in fieldValues.split('"') if s.strip() != '']

        output = []
        if len(outputA[0].split()) > 1:
            outputB = outputA[0].split()
            output.append(outputB[0])
            output.append(outputB[1])

            for i in range(2,len(outputA)+1):
                output.append(outputA[i-1].strip())

            cleaned[0] = output[0]
        else:
            cleaned[0] = outputA[0]

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

