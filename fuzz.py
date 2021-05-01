import subprocess
#The example cases only work when there is a already logged
#in user named n with the password qw2
#Need to include the EXT command at the end of every fuzz in input

def fuzz():
    """Does the fuzzing"""

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
    for i in range(len(output)):
        if answers[i] in output[i]:
            continue
        else:
            print("Test Case Failed: %s != %s" %(output[i], answers[i]))
            fail = True

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

if __name__ == "__main__":
    fuzz()