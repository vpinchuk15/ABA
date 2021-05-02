import subprocess
import random
import string
#The example cases only work when there is a already logged
#in user named n with the password qw2
#Need to include the EXT command at the end of every fuzz in input

def fuzz():
    """Does the fuzzing"""

    fuzzLogin(10)
    adrANDedr(100)
    rer(100)
    delete(10)
    imd(100)
    addTestCase('EXT','OK')
    testing()
    testPass()

def testPass():
    """
    Deterimnes if the tests passed
    """

    f1 = open("output.txt", 'r')
    f2 = open("answers.txt", 'r')

    output = f1.readlines()
    answers = f2.readlines()

    f1.close()
    f2.close()

    if len(output) != len(answers):
        print("Need to reconfigure test")
        return None

    fail = False
    total =0
    for i in range(len(output)):
        if answers[i] in output[i]:
            total+=1
            continue
        else:
            print("Test Case %d Failed: %s != %s" %(total,output[i], answers[i]))
            fail = True
        total+=1

    if fail == False:
        print("All Tests Passed")

def testing():
    """Sends the input to the aba puts the output to the file"""

    myinput = open('input.txt')
    myoutput = open('output.txt', 'w')
    p = subprocess.Popen('aba.py', stdin=myinput, stdout = myoutput, stderr=myoutput, shell=True)
    p.wait()
    myoutput.flush()

def addTestCase(inputString, answer):
    f1 = open("input.txt", 'a')
    f2 =open("answers.txt", 'a')

    f1.write("\n")
    f2.write("\n")
    f1.write(inputString)
    f2.write(answer)

    f1.close()
    f2.close()

def adrANDedr(total):

    addTestCase('ADR n', "OK")

    #Greater than 64
    for i in range(total//4):
        value = 'ADR n ' + 'SN=' + '"'+ ''.join(random.choice(string.ascii_letters) for i in range(67))+ '"' + ' WEM='+ '"'+ ''.join(random.choice(string.ascii_letters) for i in range(10)) + '"'
        addTestCase(value,"One or more invalid record data fields." )

    #Puncutation
    for i in range(total//4):
        if i % 2 == 0:
            accecpt = string.punctuation.replace('"',' ')
            value = 'EDR n ' + 'SN='+ '"'+ ''.join(random.choice(accecpt) for i in range(11))+'"'
            addTestCase(value, 'OK')
    
    #Bad record iD
    for i in range(total//4):
        value = 'ADR ' + ''.join(random.choice(string.ascii_letters) for i in range(67))
        addTestCase(value, 'Invalid recordID')
    
    #Duplicate RecordID
    for i in range(total//4):
        addTestCase('ADR n',"Duplicate recordID")

def rer(total):

    #Bad recordID
    for i in range(total//4):
        value = 'RER ' + ''.join(random.choice(string.ascii_letters) for i in range(67))
        addTestCase(value, 'Invalid recordID')

    #OK ones
    for i in range(total//4):
        if i % 2 == 0:
            value = 'RER n'
            addTestCase(value, "OK")
        else:
            accecptedFieldValues = ['SN', 'GN', 'PEM', 'WEM', 'PPH', 'WPH', 'SA', 'CITY', 'STP', 'CTY', 'PC']
            value = 'RER n '
            for j in range(4):
                value= value + random.choice(accecptedFieldValues) + ' '
            addTestCase(value, "OK")


    #Bad values
    for i in range(total//4):
        value = 'RER n '
        for j in range(4):
            value= value + ''.join(random.choice(string.ascii_letters) for i in range(4)) + ' '
        addTestCase(value, "Invalid fieldname(s)")
    
    #no recordIDs
    for i in range(total//4):
        value = 'RER ' + ''.join(random.choice(string.punctuation) for i in range(7))
        addTestCase(value, 'RecordID not found')

def delete(total):
    for i in range(total):
        value = "DER " + ''.join(random.choice(string.ascii_letters) for i in range(5)) + ''.join(random.choice(string.punctuation) for i in range(5))
        addTestCase(value,'RecordID not found')


def imd(total):

    #Empty file
    f = open('testEmpty.csv', 'w')
    addTestCase('IMD testEmpty.csv', "OK")

    #Bad Data
    f1 = open('baddata.csv', 'w')
    for i in range(total//4):
        value = ''.join(random.choice(string.punctuation) for i in range(100)) + '\n'
        f1.write(value)

    addTestCase('IMD baddata.csv',"Input_file invalid format" )

def fuzzLogin(times):
    
    #Admin Log in
    #Passwords don't match

    for i in range(times):
        value = ''.join(random.choice(string.ascii_letters) for i in range (12))
        addInput(value)
        value1 = ''.join(random.choice(string.ascii_letters) for i in range (12))
        addTestCase(value1,"Passwords do not match." )

    #Now they match but >24
    for i in range(times):
        value = ''.join(random.choice(string.punctuation) for i in range (27))
        addInput(value)
        addTestCase(value,"Password contains illegal characters.")
    
    #Now they are <24 but have illegal characters
    for i in range(times):
        value = ''.join(random.choice(string.punctuation) for i in range (12))
        addInput(value)
        addTestCase(value,"Password contains illegal characters.")

    #adds password
    addInput('qw2')
    addTestCase('qw2','OK')

    #add user 'n'
    addTestCase("ADU n", "OK")
    addTestCase('LOU', "OK")

    #none user login
    addTestCase('LIN bob',"Invalid Credentials")

    #login user
    addInput('LIN n')
    addInput('qw2')
    addTestCase('qw2', 'OK')



def addInput(inputString):
    f1 = open("input.txt", 'a')

    f1.write("\n")
    f1.write(inputString)

    f1.close()

if __name__ == "__main__":
    fuzz()