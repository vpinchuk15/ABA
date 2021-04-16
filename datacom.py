#ABA Module: Database Commands
#Author: Nathan Shah
#Date: Updated: April 15, 2021
#PLEASE READ: Before intial use need to create database via datacom.UserDatabase()

import pickle

class UserDatabase:
    """
    Models the user database.
    """
    def __init__(self):
        self.users = {}
        
        open("datacomFile.txt", "x")
        with open("datacomFile.txt", "wb") as f:
            pickle.dump(self.users, f)

        f.close()
        
class User:
    """
    A class that stores the information of the given user.
    """
    def __init__(self, username):
        self.username = username
        self.contacts = {}

class Record:
    """
    The record conatins the information about a particular record.
    """
    def __init__(self, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
        self.recordID = recordID
        self.SN = SN
        self.GN = GN
        self.PEM = PEM
        self.WEM = WEM
        self.PPH = PPH
        self.WPH = WPH
        self.SA = SA
        self.CITY = CITY
        self.PC = PC

def addRecord(username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Adds a record to the given users contacts.
    """
    if not addRecordCheck(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC):
        return None
    else:
        users = openDatabase()

        users.values()

        if users.get(username, None) == None:
            users[username] = User(username)

        if len(users[username].contacts) == 256:
            print("Number of records exceeds maximum")
            return None
        
        if users[username].contacts.get(recordID, None) == None:
            users[username].contacts[recordID] = Record(recordID, SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC)
        else:
            print("Duplicate recordID")
            return None

        print("OK")
        saveDatabase(users)

def addRecordCheck(recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Validates Inputs to addRecord method
    """

    if recordID == '':
        print("No recordID")
        return False
    
    if len(recordID) > 64:
        print("Invalid recordID")
        return False

    fieldValue = [SN, GN, PEM, WEM, PPH, WPH, SA, CITY, PC]

    for value in fieldValue:
        if value == None:
            continue
        if len(value) > 64:
            print("One or more invalid record data fields")
            return False

    return True
    
def deleteRecord(username, recordID):
    """
    Deletes a record from the given users contacts.
    """

def editRecord(username, recordID):
    """
    Edits a record from the given users contacts.
    """
def readRecord(username, recordID, SN = None, GN = None, PEM = None, WEM = None, PPH = None,
                WPH = None, SA = None, CITY = None, PC = None):
    """
    Prints the requested information to the user about th record of interest.
    """

def importDatabase(username, filename):
    """
    Imports the database of contacts in the form of a csv
    """

def exportDatabase(username, filename):
    """
    Exports a users database in the form of a csv
    """

def openDatabase():
    """
    Opens the databaseFile.txt
    """
    with open("datacomFile.txt", "rb") as f:
        users = pickle.load(f)
        f.close()
    
    return users

def saveDatabase(users):
    with open("datacomFile.txt", "wb") as f:
        pickle.dump(users,f)
    
    f.close()

    return None