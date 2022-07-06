import random
#welcome to dart bot
MainM = True
#version and build number
version = "1.0"
build = "32h431c"
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
    

