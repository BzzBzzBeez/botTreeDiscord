from random import randint
from time import sleep
from datetime import datetime
import pyautogui
import cv2


def isReady():
    coords = pyautogui.locateCenterOnScreen('ready.png',confidence=0.8)
    if coords != None: 
        return True
    else:
        return False

def clickWater():
        coords = pyautogui.locateCenterOnScreen('watered.png',confidence=0.9, grayscale=False)
        if coords != None: 
            pyautogui.moveTo(coords.x, coords.y)
            pyautogui.click()
            pyautogui.moveTo(100,100)

def alreadyWatered():
        coords = pyautogui.locateCenterOnScreen('alreadyWatered.png',confidence=0.8)
        if coords != None: 
            return True
        else:
            return False

def rejeter():
        coords = pyautogui.locateCenterOnScreen('rejeter.png',confidence=0.8)
        if coords != None: 

            pyautogui.moveTo(coords.x, coords.y)
            pyautogui.click()
            pyautogui.moveTo(100,100)

def rejeter2():
        coords = pyautogui.locateCenterOnScreen('rejeter2.png',confidence=0.8)
        if coords != None: 

            pyautogui.moveTo(coords.x, coords.y)
            pyautogui.click()
            pyautogui.moveTo(100,100)

def changeAccountTo1():
    pyautogui.moveTo(175, 1018)
    pyautogui.click()
    sleep(.5)

    coords = pyautogui.locateCenterOnScreen('change_account.png',confidence=0.8) # Change account
    if coords != None: 

        pyautogui.moveTo(coords.x, coords.y)
        sleep(.5)

        pyautogui.moveTo(406,947)
        pyautogui.click()

def changeAccountTo0():
    pyautogui.moveTo(175, 1018)
    pyautogui.click()
    sleep(.5)

    coords = pyautogui.locateCenterOnScreen('change_account.png',confidence=0.8) # Change account
    if coords != None: 

        pyautogui.moveTo(coords.x, coords.y)
        sleep(.5)

        pyautogui.moveTo(406,910)
        pyautogui.click()

def goToTreeChannel():
    coords = pyautogui.locateCenterOnScreen('coin.png',confidence=0.8) # Go To COIN
    if coords != None: 

        pyautogui.moveTo(coords.x, coords.y)
        pyautogui.click()
        sleep(.5)

        coords = pyautogui.locateCenterOnScreen('tree_channel.png',confidence=0.8) # Go To tree channel
        if coords != None: 

            pyautogui.moveTo(coords.x, coords.y)
            pyautogui.click()
            sleep(.5)

def collectApples():
    for coords in pyautogui.locateAllOnScreen('soup.png',confidence=0.9, grayscale=False): # Find soups
        if coords != None: 

            pyautogui.moveTo(coords[0]+30, coords[1]+20, 0.2)
            pyautogui.click()
            print("    Apple collected")
            sleep(.2)
#-------------------------------
# ajout -> si passer un niveau apres watered, retirer2 avant de check les pommes

now = datetime.now()

today3am = now.replace(hour=3, minute=0)
today8am = now.replace(hour=8, minute=0)

print(pyautogui.position())
print(pyautogui.size())
sleep(1)
i = 0 # Iteration
a = 1 # Modulo % 2 / Pair impair

#goToTreeChannel()

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if now < today8am and now > today3am:
        print("3h < Now < 8h")

        goToTreeChannel()
        if isReady():
            print("Ready ! : ")
            rejeter() #IF REJETER NOT DELETED
            rejeter2() # IF LVL UP

            clickWater()
            print(" Clicking")
            rejeter() #IF REJETER NOT DELETED
            rejeter2() # IF LVL UP
            sleep(.5)

            if alreadyWatered():
                rejeter()
                print("  Rejecting...")
                sleep(.5)

                if a % 2 == 0:
                    changeAccountTo1()
                    sleep(5)
                    print("  Account Switched to 1")
                    goToTreeChannel()
                    print("   Go to COIN")
                else:
                    changeAccountTo0()
                    sleep(5)
                    print("  Account Switched to 0")
                    goToTreeChannel()
                    print("  Go to COIN")
                
                a = a + 1 #Change accounts (a % 2)

            else:
                print("[Watered]")
                sleep(5)
                
                print("  Apples checking")
                collectApples()
                
                if a % 2 == 0:
                    changeAccountTo1()
                    sleep(5)
                    print("  Account Switched to 1")
                    goToTreeChannel()
                    print("  Go to COIN")
                else:
                    changeAccountTo0()
                    sleep(5)
                    print("  Account Switched to 0")
                    goToTreeChannel()
                    print("  Go to COIN")
                
                a = a + 1 #Change accounts (a % 2)

        else:
            i = i+1 #Print Iteration
            print(str(i))
        
    sleep(1)
