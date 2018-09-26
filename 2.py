import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color=[0.12,0.12,0.12], units='pix', size=[1500,1500], allowGUI=False, fullscr=False)#creates a window 
myClock = core.Clock() #this creates and starts a clock which we can later read

movingLilac = visual.Circle(myWin, radius=15, fillColor=[1, 0.15, 0.15], lineColor=None)
movingGreen = visual.Circle(myWin, radius=15, fillColor=[1, 0.12, 1], lineColor=None)
fixation = visual.TextStim(myWin, text='+', height=18, color='black') 

myScale = visual.RatingScale(myWin, pos=[0, -360], low=-20, high=20,  textSize=0.5, lineColor='black',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
information=visual.TextStim(myWin, pos=[0,-385], text='', height=18, color='black') 
title=visual.TextStim(myWin, pos=[0,305], text='Lilac Chaser Illusion', height=24, color='white') 

# draw twelve circles but skip one of them (so draw eleven)
def drawDisks(radius, missingOne):

    missingAngle = 90 * missingOne
    for angle in range(0, 270, 15):
        angleR = math.radians(angle)
        x =math.cos(angleR) * radius
        y =math.sin(angleR) * radius
        movingLilac.setPos([x,y])

        x =math.cos(angleR) * (radius + 120)
        y =math.sin(angleR) * (radius + 60)
        movingGreen.setPos([x,y])

        if angle != missingAngle:
            movingLilac.draw()
            movingGreen.draw()

# the main loop
def mainLoop(radius=300):
    
    finished = False
    missingOne =0
    showOnlyIllusion = False
    movingGreen.opacity = 0

    while not finished:

        drawDisks(radius, missingOne)
        missingOne = missingOne +1
        if missingOne == 12:
           missingOne =0

        fixation.draw()

        if showOnlyIllusion ==False:
            title.draw()
            myScale.draw()
            information.draw()
        myWin.flip()

        if myScale.noResponse ==False: #some new value has been selected with the mouse
            backColour = myScale.getRating()
            rgb = [backColour / 200., backColour / 300., backColour / 600.]
            myWin.color = rgb
            information.setText(str(backColour))
            myScale.reset()

        pressedList =event.getKeys(keyList=['escape','a','s']) #pressing ESC quits the program
        if len(pressedList) >0:
            if pressedList[0] =='escape':
                finished =True
            elif pressedList[0] =='a':
                movingGreen.opacity = abs(movingGreen.opacity - 1)
            elif pressedList[0] =='s':
                showOnlyIllusion = not showOnlyIllusion
            event.clearEvents()

        waitUntil = myClock.getTime() + 0.6
        while myClock.getTime() <waitUntil:
            pass

mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits





