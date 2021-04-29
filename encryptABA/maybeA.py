#ABA Module: Audit Log
#Author: Nathan Shah, Dominic Santilla
#Date: Updated: April 15, 2021
#PLEASE READ: Before intial use need to create database via auditlog.AuditLog()

import pickle
from collections import deque
from datetime import datetime
from datetime import date as d
from cryptography.fernet import Fernet #noqa

class AuditLog():
    """
    Models the audit log
    """
    def __init__(self):
        self.log = deque(maxlen=512)

        try:
            self.key = Fernet(Fernet.generate_key())
            self.saveLog(self.log)
        except FileExistsError:
            return None

    def openLog(self):
        """
        Opens the auditlog.txt
        """
        # opening the encrypted file
        with open('logFile.txt', 'rb') as enc_file:
            encrypted = enc_file.read()
  
        # decrypting the file
        decrypted = self.key.decrypt(encrypted)
  
        # opening the file in write mode and
        # writing the decrypted data
        with open('logFile.txt', 'wb') as dec_file:
            dec_file.write(decrypted)

        with open("logFile.txt", "rb") as f:
            log = pickle.load(f)
            f.close()
        
        return log

    def saveLog(self,log):
        with open("logFile.txt", "wb") as f:
            pickle.dump(log,f)
        
        f.close()

        with open('logFile.txt', 'rb') as file:
            original = file.read()
        
        # encrypting the file
        encrypted = self.key.encrypt(original)
    
        # opening the file in write mode and 
        # writing the encrypted data
        with open('logFile.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

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

def addLog(AuditLog,recordType, userID):
    """
    Adds record to the log
    """
    log = AuditLog.openLog()

    log.append(Record(recordType, userID))

    AuditLog.saveLog(log)

    return None

def displayLog(AuditLog,specified_ID = None):
    """
    Displays the log and log entries
    """
    log = AuditLog.openLog()
    AuditLog.saveLog(log)

    for record in log:
        if specified_ID == None or record.userID == specified_ID:
            print("%s, %s, %s, %s" %(record.date, record.time, record.recordType, record.userID))

    return None
    