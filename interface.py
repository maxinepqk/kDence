from tkinter import *
import time, decimal
import threading as thr
from audio import play

def roundHalfUp(d): # taken from course notes
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue): # taken from course notes
    return "#%02x%02x%02x" % (red, green, blue)

def init(data):
    data.mode = "main"
    data.cx = data.width//2
    data.cy = data.height//2

    data.blue0 = rgbString(219, 226, 240)
    data.blue1 = rgbString(181, 197, 212)
    data.blue2 = rgbString(128, 153, 176)
    data.blue3 = rgbString(86, 117, 147)
    data.blue4 = rgbString(52, 87, 120)
    data.blue5 = rgbString(25, 59, 91)

    data.circleX = data.cx
    data.circleY = data.cy
    data.circleMinR = 20
    data.circleMaxR = 60
    data.circleR = data.circleMinR
    data.circleTimeI = -1
    data.circleSpeed = 8

    data.rhythm = []
    data.music = "sounds/beats/BDRUM13.wav"
    data.recordCounter = 0
    data.replayCounter = 0

    data.keysImage = PhotoImage(file="pics/keys.gif")
    data.keysImageHeight = 456
    data.keysImageWidth = 800
    data.notePlaying = "C0"
    data.notesToMusic = {}
    data.notesTime = []
    data.notesPlayed = []

## Mode Dispatcher
def mousePressed(event, data):
    if (data.mode == "main"): mainMousePressed(event, data)
    elif (data.mode == "recordBeatStart"): recordBeatStartMousePressed(event, data)
    elif (data.mode == "recordBeatEnd"): recordBeatEndMousePressed(event, data)
    elif (data.mode == "replay"): replayMousePressed(event, data)
    elif (data.mode == "recordMelStart"): recordMelStartMousePressed(event, data)
    elif (data.mode == "recordMelEnd"): recordMelEndMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "main"): mainKeyPressed(event, data)
    elif (data.mode == "recordBeatStart"): recordBeatStartKeyPressed(event, data)
    elif (data.mode == "recordBeatEnd"): recordBeatEndKeyPressed(event, data)
    elif (data.mode == "replay"): replayKeyPressed(event, data)
    elif (data.mode == "recordMelStart"): recordMelStartKeyPressed(event, data)
    elif (data.mode == "recordMelEnd"): recordMelEndKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "main"): mainTimerFired(data)
    elif (data.mode == "recordBeatStart"): recordBeatStartTimerFired(data)
    elif (data.mode == "recordBeatEnd"): recordBeatEndTimerFired(data)
    elif (data.mode == "replay"): 
        replayingTimer= thr.Thread(target = replayTimerFired, args = (data,))
        replayingTimer.start()
    elif (data.mode == "recordMelStart"): recordMelStartTimerFired(data)
    elif (data.mode == "recordMelEnd"): recordMelEndTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "main"): mainRedrawAll(canvas, data)
    elif (data.mode == "recordBeatStart"): recordBeatStartRedrawAll(canvas, data)
    elif (data.mode == "recordBeatEnd"): recordBeatEndRedrawAll(canvas, data)
    elif (data.mode == "replay"): replayRedrawAll(canvas, data)
    elif (data.mode == "recordMelStart"): recordMelStartRedrawAll(canvas, data)
    elif (data.mode == "recordMelEnd"): recordMelEndRedrawAll(canvas, data)

## MATH FUNCTIONS

def almostEqual(d1, d2, epsilon=10**-6): # cited from cs112_f16 test code
    return (abs(d2 - d1) < epsilon)

def almostLessThanOrEqual(d1, d2, epsilon=10**-6):
    return ((d1 - d2) < epsilon) # test for d1 <= d2

## AUDIO FUNCTIONS

def playMusic(data):
    playing = thr.Thread(target = play, args = (data.music,))
    playing.start()

def getTimeDiff(data, whichList):
    data.tDiff = [0]
    for i in range(1,len(whichList)):
        t = whichList[i] - whichList[i-1]
        data.tDiff.append(t) # gets the difference in time

def replayRhythm(data, whichList):
    data.music = "sounds/beats/BDRUM13.wav"
    getTimeDiff(data, whichList) # returns a list of time differences between each beat
    print(data.tDiff)
    playMusic(data) # plays the sound
    for t in data.tDiff:
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playMusic(data)
                break

def replayMelody(data, whichList):
    getTimeDiff(data, whichList) # returns a list of time differences between each beat
    data.music = data.notesToMusic[data.notesPlayed[0]]
    playMusic(data) # plays the sound
    for t in data.tDiff:
        i = data.tDiff.index(t)
        data.music = data.notesToMusic[data.notesPlayed[i]]
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playMusic(data)
                break

## MAIN MODE
def mainMousePressed(event, data): pass

def mainKeyPressed(event, data):
    if (event.keysym == "r"): 
        data.mode = "recordBeatStart"
        data.music = "sounds/beats/BDRUM13.wav"
        data.rhythm.clear()
        data.recordCounter = 0
    if (event.keysym == "m"):
        makeNotesToMusic(data)
        data.mode = "recordMelStart"


def mainTimerFired(data): pass

def mainRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    msg1 = "Press r to record a beat!"
    canvas.create_text(data.cx, data.cy-20, text = msg1, font = "Arial 30 italic",
                       fill = data.blue4)
    msg2 = "Press m to record a melody!"
    canvas.create_text(data.cx, data.cy+20, text = msg2, font = "Arial 30 italic",
                       fill = data.blue4)


## RECORD BEAT START MODE
def recordBeatStartMousePressed(event, data): pass

def recordBeatStartKeyPressed(event, data):
    if (event.keysym == "space"):
        playMusic(data)
        data.rhythm.append(time.time())
    elif (event.keysym == "p"):
        data.mode = "replay"
        replayRhythm(data, data.rhythm)

def recordBeatStartTimerFired(data):
    data.recordCounter += 1
    if (data.recordCounter > 50): data.mode = "recordBeatEnd"

def recordBeatStartDrawTitle(canvas, data):
    canvas.create_text(data.cx, data.cy-40, text = "Recording", 
                       font = "Arial 40 italic", fill = data.blue4)

def recordBeatStartDrawTimer(canvas, data):
    countDown = 5 - data.recordCounter//10
    if (countDown < 0): countDown = 0
    canvas.create_text(data.cx, data.cy + 40, text=str(countDown),
                       font = "Arial 30 italic", fill = data.blue4)

def recordBeatStartRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    recordBeatStartDrawTitle(canvas, data)
    recordBeatStartDrawTimer(canvas, data)


## RECORD BEAT END MODE
def recordBeatEndMousePressed(event, data): pass

def recordBeatEndKeyPressed(event, data):
    if (event.keysym == "p"):
        replaying = thr.Thread(target = replayRhythm, args = (data, data.rhythm))
        replaying.start()
        data.mode = "replay"
        
    elif (event.keysym == "r"): 
        data.rhythm.clear()
        data.recordCounter = 0
        data.mode = "recordBeatStart"

def recordBeatEndTimerFired(data): pass

def recordBeatEndRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    canvas.create_text(data.cx, data.cy-40, text = "Finished",
                       font = "Arial 40 italic", fill = data.blue4)
    msg = "Press p to replay, r to record again!"
    canvas.create_text(data.cx, data.cy+40, text = msg, font = "Arial 30 italic",
                       fill = data.blue4)


## REPLAY MODE
def replayMousePressed(event, data): pass

def replayKeyPressed(event, data):
    if (event.keysym == "p"): 
        data.mode = "replay"
        replayRhythm(data, data.rhythm)
    elif (event.keysym == "r"): 
        data.rhythm.clear()
        data.recordCounter = 0
        data.replayCounter = 0
        data.circleR = data.circleMinR
        data.mode = "recordBeatStart"

def replayExpandCircle(data):
    if (data.circleTimeI < len(data.tDiff)):
        t = (data.tDiff[data.circleTimeI])/2
        if (t == 0): t = 0.5
        data.circleSpeed = roundHalfUp((data.circleMaxR - data.circleMinR)/(10*t))
        
    else: data.mode = "main"

def replayTimerFired(data):
    
    if (data.replayCounter > 55): data.mode = "main" #added the previous 0.5s to expand
    #elif (data.replayCounter % 5 == 0):
    data.circleR += data.circleSpeed # convert to milliseconds
    #print("r", data.circleR)
    data.replayCounter += 1
    if (data.circleR >= data.circleMaxR): data.circleSpeed *= -1
    elif (data.circleR <= data.circleMinR):
        data.circleTimeI += 1
        data.circleR = data.circleMinR
        replayExpandCircle(data)
        #print("speed", data.circleSpeed)
        if (data.circleSpeed < 0): data.circleSpeed *= -1 # initial expansion
        
def replayDrawText(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    canvas.create_text(data.cx, data.cy-40, text = "Replaying",
                       font = "Arial 40 italic", fill = data.blue4)

def replayDrawExpandingCircle(canvas, data):
    (cx, cy, r) = (data.circleX, data.circleY, data.circleR)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = "black")

def replayRedrawAll(canvas, data):
    replayDrawText(canvas, data)
    replayDrawExpandingCircle(canvas, data)


## RECORD MELODY START
def makeNotesToMusic(data):
    notes = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "G#0", 
             "A0", "A#0", "B0"]
    for note in notes:
        data.notesToMusic[note] = "sounds/notes/%s.wav" %note

def recordMelStartMousePressed(event, data):
    #print(event.x, event.y)
    if (event.x > 210 and event.x < 995 and event.y > 300 and event.y < 630): #playing keybaord
        if ((event.x > 213 and event.x < 235 and event.y > 303 and event.y < 500) or
            (event.x > 213 and event.x < 250 and event.y > 503 and event.y < 625)):
            data.notePlaying = "C0"
        elif (event.x > 239 and event.x < 258 and event.y > 304 and event.y < 497):
            data.notePlaying = "C#0"
        elif ((event.x > 265 and event.x < 286 and event.y > 303 and event.y < 500) or
            (event.x > 258 and event.x < 296 and event.y > 503 and event.y < 625)):
            data.notePlaying = "D0"
        elif (event.x > 295 and event.x < 315 and event.y > 307 and event.y < 493):
            data.notePlaying = "D#0"
        elif ((event.x > 319 and event.x < 337 and event.y > 302 and event.y < 499) or
            (event.x > 300 and event.x < 337 and event.y > 508 and event.y < 625)):
            data.notePlaying = "E0"
        elif ((event.x > 341 and event.x < 365 and event.y > 303 and event.y < 503) or
            (event.x > 345 and event.x < 380 and event.y > 503 and event.y < 625)):
            data.notePlaying = "F0"
        elif (event.x > 370 and event.x < 390 and event.y > 305 and event.y < 500):
            data.notePlaying = "F#0"
        elif ((event.x > 395 and event.x < 410 and event.y > 302 and event.y < 500) or
            (event.x > 387 and event.x < 423 and event.y > 505 and event.y < 620)):
            data.notePlaying = "G0"
        if (event.x > 416 and event.x < 439 and event.y > 310 and event.y < 500):
            data.notePlaying = "G#0"
        elif ((event.x > 423 and event.x < 460 and event.y > 303 and event.y < 500) or
            (event.x > 432 and event.x < 465 and event.y > 505 and event.y < 620)):
            data.notePlaying = "A0"
        elif (event.x > 465 and event.x < 490 and event.y > 305 and event.y < 500):
            data.notePlaying = "A#0"
        elif ((event.x > 495 and event.x < 512 and event.y > 303 and event.y < 500) or
            (event.x > 475 and event.x < 510 and event.y > 505 and event.y < 625)):
            data.notePlaying = "B0"

        data.notesTime.append(time.time())
        data.notesPlayed.append(data.notePlaying)
        data.music = data.notesToMusic[data.notePlaying]
        playMusic(data)


def recordMelStartKeyPressed(event, data):
    print(event.keysym)

def recordMelStartTimerFired(data):
    data.recordCounter += 1
    if (data.recordCounter > 50): data.mode = "recordMelEnd"

def recordMelStartRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    centeredx = data.width//2 - data.keysImageWidth//2
    centeredy = data.height//4
    canvas.create_image(centeredx, centeredy, anchor=NW, image=data.keysImage)

## RECORD MELODY END
def recordMelEndMousePressed(event, data): pass

def recordMelEndKeyPressed(event, data):
    if (event.keysym == "p"):
        replaying = thr.Thread(target = replayMelody, args = (data, data.notesTime))
        replaying.start()
        data.mode = "replay"

def recordMelEndTimerFired(data): pass
def recordMelEndRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.blue0)
    canvas.create_text(data.cx, data.cy-40, text = "Finished",
                       font = "Arial 40 italic", fill = data.blue4)
    msg = "Press p to replay, r to record again!"
    canvas.create_text(data.cx, data.cy+40, text = msg, font = "Arial 30 italic",
                       fill = data.blue4)

####################################
# use the run function as-is
####################################

def run(width=300, height=300): # taken from course notes
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the root and the canvas
    root = Tk()
    init(data) # changed placement of init to load images
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)
    