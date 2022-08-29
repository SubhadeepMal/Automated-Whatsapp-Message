# import pywhatkit as kit
# for x in range(10):
#     kit.sendwhatmsg("+919002794950", "@#$$@%^#^#", 22, 54)
import pyautogui as pg
import time
timeLimit=int(input("Time Limit: "))
messsage=input("Enter the message: ")

x=0
while x<timeLimit:
    pg.typewrite(messsage)
    pg.press("Enter")
    x+=1
    
