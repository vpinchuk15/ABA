#ABA Module: Audit Log
#Author: Nathan Shah, Dominic Santilla
#Date: Updated: April 15, 2021
#PLEASE READ: Before intial use need to create database via auditlog.AuditLog()
#Changed line 58 end="" <- delete after fuzzing

import pickle
from collections import deque
from datetime import datetime
from datetime import date as d

class AuditLog():
    """
    Models the audit log
    """
    def __init__(self):
        self.log = deque(maxlen=512)

        try:
            open("logFile.txt", "x")
            with open("logFile.txt", "wb") as f:
                pickle.dump(self.log, f)

                f.close()
        except FileExistsError:
            return None

class Record:
    """
    Stores information about the given action
    """
    def __init__(self, recordType, userID):
        self.date = d.today().strftime("%m/%d/%y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.recordType = recordType
        self.userID = userID

def addLog(recordType, userID):
    """
    Adds record to the log
    """
    log = openLog()

    log.append(Record(recordType, userID))

    saveLog(log)

    return None

def displayLog(specified_ID = None):
    """
    Displays the log and log entries
    """
    log = openLog()

    for record in log:
        if specified_ID == None or record.userID == specified_ID:
            print("%s, %s, %s, %s" %(record.date, record.time, record.recordType, record.userID), end="")

    print("OK")
    return None
    
def openLog():
    """
    Opens the logFile.txt
    """
    with open("logFile.txt", "rb") as f:
        log = pickle.load(f)
        f.close()
    
    return log

def saveLog(log):
    with open("logFile.txt", "wb") as f:
        pickle.dump(log,f)
    
    f.close()

    return None