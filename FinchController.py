from BirdBrain import Finch
import time
import random
import pynput
from pynput import keyboard

myFinch = Finch()

myFinch.playNote(60,0.5)

lights = False

availableChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!1234567890.,'
numChars = '1234567890'
def finchFunc(msg,isStop):
    if isStop == True:
        myFinch.stopAll()
    for i in range(len(msg)):
        if msg[i] in availableChars:
            myFinch.print(msg[i])
        time.sleep(0.5)

def freeRoam(units):
    thing = True
    u = 0
    while thing == True:
        dist = myFinch.getDistance()
        print(dist)
        if dist > 20:
            myFinch.setMotors(50,50)
        else:
            ran = random.randrange(1,2)
            if ran == 1:
                myFinch.setMotors(-30,30)
            elif ran == 2:
                myFinch.setMotors(30,-30)
        u += 1
        if u == units:
            thing = False
            myFinch.setMotors(0,0)
    pass

def InteractiveSystem(firstTime):
    cmdTable = ['help','finch','code','stop_finch','keybinds','quit']
    if firstTime == True:
        print('KEWI INTERACTIVE PROGRAM(v1.0)™')
    print('----------------------------------------------------------------------')
    print("Say 'help' if you need help with the finch/code.")
    print("Say 'quit' to exit the Interactive System.")
    response = input('Say a command (capital sensitive): ')
    if response == 'help':
        print('Commands for help:')
        print('keybinds  |  code')
        print('finch     |  stop_finch')
        r2 = input('What do you need help with?: ')
        if r2 == 'keybinds':
            print('Keybinds:')
            print('w,a,s,d - Responsible for moving the finch')
            print('m - Displaying a message of your choice on the finch')
            print('h - Makes a honking noise on the finch (alerts others of the finch)')
            print('l - Turns on the lights of the finch')
            print('L - Turns off the lights of the finch')
            print('f - Turns on freeroam mode for the finch and moves for however long you want it to')
            print('t - Makes you able to run different commands on the finch (in progress, not everything will work on this)')
            print("q - Stops the finch's current actions (might not work for some functions)")
        elif r2 == 'code':
            print('The finch uses python, which is a common coding language')
            print('For more help with the finch go to these sites:')
            print('https://learn.birdbraintechnologies.com/finch/python/')
            print('https://www.python.org/')
        elif r2 == 'finch':
            print('Information about the finch:')
            print("The finch robot runs off of python, and the main file is 'BirdBrain.py'")
            print('The finch consists of a motherboard with lights that is exposed, 2 front sensors, 1 bottom sensor, 2 buttons, and more.')
            print('For more information about the finch go here: https://learn.birdbraintechnologies.com/finch/python/')
        elif r2 == 'stop_finch':
            print('Emergency stops the finch')
        elif r2 not in cmdTable:
            print('Command does not exist!')
            time.sleep(1.5)
            InteractiveSystem(False)
            pass
    elif response == 'stop_finch':
        finchFunc('FinchStopped',True)
        myFinch.stop()
    elif response == 'quit':
        print('Exiting the program...')
        pass
    else:
        if response not in cmdTable:
            print('Command does not exist!')
        time.sleep(1.5)
        InteractiveSystem(False)
    pass


def on_release(key):
    if key == keyboard.KeyCode(None,'w'):
        myFinch.setMotors(0,0)
    if key == keyboard.KeyCode(None,'s'):
        myFinch.setMotors(0,0)
    if key == keyboard.KeyCode(None,'a'):
        myFinch.setMotors(0,0)
    if key == keyboard.KeyCode(None,'d'):
        myFinch.setMotors(0,0)
speed = 50
clutch = 1
speed1 = property(speed)
clutch1 = property(clutch)
def on_pressed(key):
    if key == keyboard.KeyCode(None,'w'):
        myFinch.setMotors(speed1.fget,speed1.fget)
    if key == keyboard.KeyCode(None,'s'):
        myFinch.setMotors(-speed1.fget,-speed1.fget)
    if key == keyboard.KeyCode(None,'a'):
        myFinch.setMotors(-speed1.fget-10,speed1.fget-20)
    if key == keyboard.KeyCode(None,'d'):
        myFinch.setMotors(speed1.fget-20,-speed1.fget-10)
    if key == keyboard.KeyCode(None,'m'):
        message = input('Enter a message: ')
        if message:
            print('Saying, ' + message)
            finchFunc(message,False)
    if key == keyboard.KeyCode(None,'h'):
        myFinch.playNote(60,0.5)
    if key == keyboard.KeyCode(None,'l'):
        myFinch.setBeak(100, 100, 100)
    if key == keyboard.KeyCode(None,'L'):
        myFinch.setBeak(0, 0, 0)
    if key == keyboard.KeyCode(None,'f'):
        dist = input('How far do you want to travel? (units): ')
        confirmDist = ''
        for i in range(len(dist)):
            if dist[i] in numChars:
                confirmDist += str(dist[i])
        freeRoam(int(confirmDist))
    if key == keyboard.KeyCode(None, 't'):
        InteractiveSystem(True)
    if key == keyboard.KeyCode(None,'c'):
        print(clutch1.fget)
        extravar = clutch1.fget
        extraspeed = speed1.fget
        if clutch1.fget < 5:
            print(extravar)
            extravar += 1
            extraspeed += 10
            clutch1.setter(extravar)
            speed1.setter(extraspeed)
            print(clutch1.fget)
    if key == keyboard.KeyCode(None,'C'):
        extravar1 = clutch1.fget
        extraspeed1 = speed1.fget
        if clutch1.fget > 1:
            extravar1 += 1
            extraspeed1 += 10
            clutch1.fset(extravar1)
            speed1.setter(extraspeed1)
            print(clutch1.fget)
    if key == keyboard.KeyCode(None,'q'):
        finchFunc('FinchStopped',True)
with keyboard.Listener(
        on_press=on_pressed,
        on_release=on_release) as listener:
    listener.join()