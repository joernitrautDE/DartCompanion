import random
#welcome to dart bot
MainM = True
#version and build number
#check if number is an integer
def isInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

version = "1.0"
build = "32h506f"
#dart bot
def randomThrow():
    #random throw
    score = 0
    scoretext = ""
    field = random.randint(1,22)
    if(field == 1):
        score = 1 
    if(field == 2):
        score = 2
    if(field == 3):
        score = 3
    if(field == 4):
        score = 4
    if(field == 5):
        score = 5
    if(field == 6):
        score = 6
    if(field == 7):
        score = 7
    if(field == 8):
        score = 8
    if(field == 9):
        score = 9
    if(field == 10):
        score = 10
    if(field == 11):
        score = 11
    if(field == 12):
        score = 12
    if(field == 13):
        score = 13
    if(field == 14):
        score = 14
    if(field == 15):
        score = 15
    if(field == 16):
        score = 16
    if(field == 17):
        score = 17
    if(field == 18):
        score = 18
    if(field == 19):
        score = 19
    if(field == 20):
        score = 20
    if(field == 21):
        score = 25
    if(field == 22):
        score = 50
    type = random.randint(1, 3)
    if(type == 1):
        score = score * 1
        scoretext = "S"+str(field)
    if(type == 2):
        score = score * 2
        scoretext = "D"+str(field)
    if(type == 3):
        score = score * 3
        scoretext = "T"+str(field)
    
    print(score)
    print(scoretext)
def inputThrow():
    print("Input your throw")
    print("Syntax: 1st: type of field (S=single; D=double; T=tribble) 2nd: number of field (1-20; 25; 50)")
    print("Example: S17")
    validinput=False
    while validinput == False:
        throw = input("Enter thow!")
        throw=throw.upper()
        if(len(throw)<4 and len(throw)>1):
            if(throw[0]=="S"):
                throw=throw[1:]
                if(isInt(throw)):
                    if(int(throw)>0 and int(throw)<21 or int(throw)==25):
                        validinput=True
                        return int(throw)
                    else: 
                        print("Invalid input! (Impossible Throw) Valid: 1-20, 25")
                else:
                    print("Valid Indicator but Invalid input after! Try again!")
            elif(throw[0]=="D"):
                throw=throw[1:]
                if(isInt(throw)):
                    if(int(throw)>0 and int(throw)<21 or int(throw)==25):
                        validinput=True
                        throw=int(throw)*2
                        return int(throw)
                    else: 
                        print("Invalid input! (Impossible Throw) Valid: 1-20, 25")
                else:
                    print("Valid Indicator but Invalid input after! Try again!")
            elif(throw[0]=="T"):
                throw=throw[1:]
                if(isInt(throw)):
                    if(int(throw)>0 and int(throw)<21):
                        validinput=True
                        throw=int(throw)*3
                        return int(throw)
                    else: 
                        print("Invalid input! (Impossible Throw) Valid: 1-20")
                else:
                    print("Valid Indicator but Invalid input after! Try again!")
            else:
                print("Invalid or missing indicator of field type (S; D; T) Try again!")
        else:
            print("Invalid input! Try again!")
            
print("---<>---")
print("DartCompanion by joernitrautDE")
print("Version: "+version+" Build: "+build)
print("---<>---")
print("Available modes:")
print("1) Count down (Classic)")
print("2) Play against each other")
print("3) Play against computer")
print("4) Exit")
while MainM == True:
    modeM = input("Choose a mode to start (1-4)")
    print(modeM)
    if(isInt(modeM) == True):
        if(int(modeM) == 1):
            print("Count down mode selected")
            MainM=False
            Mode1=True
            while Mode1 == True: 
                inputloop=True
                while inputloop == True:
                    player = input("How much player? (1-2)")
                    if(isInt(player) == True):
                        print(player)
                        if(int(player) > 0 and int(player)<3):
                            inputloop=False
                        else: 
                            print("invalid input! Try again!")                    
                    else: 
                        print("invalid input! Try again!")
                #programm start
                print("Continue Programm.")
                print(player)
                if(int(player)==1):
                    validinput=False
                    while(validinput==False):
                        print("Start count?")
                        print("1) 101")
                        print("2) 301")
                        print("3) 501")
                        startcount=0
                        start=input("Select a start count! (1-3)")   
                        if(isInt(start)):
                            if(int(start)>0 and int(start)<4):
                                validinput=True
                                print(start)
                                if(int(start)==1):
                                    startcount=101
                                if(int(start)==2):
                                    startcount=301
                                if(int(start)==3):
                                    startcount=501
                            else:
                                print("invalid input! Try again!")
                        else:
                            print("invalid input! Try again!")
                    print(startcount)
                    print("Start count: "+str(startcount))
                    while startcount != 0:
                        print("Player 1, 3 throws. Throw!")
                        throws=0
                        trithrows=3
                        while trithrows != 0:
                            throws=throws+1
                            randomThrow()
                            trithrows=trithrows-1

        elif(int(modeM) == 2):
            print("Play against each other mode selected")
            MainM=False
            print(inputThrow())
        elif(int(modeM) == 3):
            print("Play against computer mode selected")
            MainM=False
        elif(int(modeM) == 4):
            print("Exiting")
            MainM=False
            exit
        else:
            print("Invalid input! Try again! (1-4)")

