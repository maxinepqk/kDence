############################# LAUNCHER ##############################

from tkinter import *
import time, decimal
import threading as thr
import os, os.path
from audio import play
from helperfunctions import rgbString
from main import mainMousePressed, mainKeyPressed, mainTimerFired, mainRedrawAll
from play import playMousePressed, playKeyPressed, playTimerFired, playRedrawAll
from playAddInstrument import (playAddInstrumentMousePressed, 
playAddInstrumentKeyPressed, playAddInstrumentTimerFired, 
playAddInstrumentRedrawAll)
from playAddDrums import (playAddDrumsMousePressed, playAddDrumsKeyPressed, 
playAddDrumsTimerFired, playAddDrumsRedrawAll)
from recordDrumsStart import (recordDrumsStartMousePressed, 
recordDrumsStartKeyPressed, recordDrumsStartTimerFired, 
recordDrumsStartRedrawAll)
from recordEnd import (recordEndMousePressed, recordEndKeyPressed, 
recordEndTimerFired, recordEndRedrawAll)
from playAddSynth import (playAddSynthMousePressed, playAddSynthKeyPressed, 
playAddSynthTimerFired, playAddSynthRedrawAll)
from recordSynthStart import (recordSynthStartMousePressed, recordSynthStartKeyPressed,
recordSynthStartTimerFired, recordSynthStartRedrawAll)
from playAddVoice import (playAddVoiceMousePressed, playAddVoiceKeyPressed, 
playAddVoiceTimerFired, playAddVoiceRedrawAll)
from recordVoiceStart import (recordVoiceStartMousePressed, 
recordVoiceStartKeyPressed, recordVoiceStartTimerFired, 
recordVoiceStartRedrawAll)
from playAddDrumsMetro import (playAddDrumsMetroMousePressed, 
playAddDrumsMetroKeyPressed, playAddDrumsMetroTimerFired, 
playAddDrumsMetroRedrawAll)
from playAddSynthMetro import (playAddSynthMetroMousePressed, 
playAddSynthMetroKeyPressed, playAddSynthMetroTimerFired, 
playAddSynthMetroRedrawAll)
from playAddVoiceMetro import (playAddVoiceMetroMousePressed, 
playAddVoiceMetroKeyPressed, playAddVoiceMetroTimerFired, 
playAddVoiceMetroRedrawAll)
from helpScreen import (helpScreenMousePressed, helpScreenKeyPressed, 
helpScreenTimerFired, helpScreenRedrawAll)
#from replayingStart import (replayingStartMousePressed, replayingStartKeyPressed,
#replayingStartTimerFired, replayingStartRedrawAll)

def init(data):
    data.mode = "main"
    data.cx = data.width//2
    data.cy = data.height//2

    data.blue0 = rgbString(219, 226, 240)
    data.blue05 = rgbString(198, 230, 244)
    data.blue07 = rgbString(179, 226, 247)
    data.blue1 = rgbString(181, 197, 212)
    data.blue15 = rgbString(128, 194, 223)
    data.blue2 = rgbString(128, 153, 176)
    data.blue3 = rgbString(86, 117, 147)
    data.blue4 = rgbString(52, 87, 120)
    data.blue5 = rgbString(25, 59, 91)

    data.startButtonPos = (data.cx-50, data.cy + 40)
    data.openButtonPos = (data.cx+50, data.cy + 40)
    data.picBG = PhotoImage(file = "pics/mainBackground.gif")
    data.playButtonR = 20

    data.picDrums = PhotoImage(file = "pics/drums.gif")
    data.picSynth = PhotoImage(file = "pics/synth.gif")
    data.picVoice = PhotoImage(file = "pics/voice.gif")
    data.picSmallKeys = PhotoImage(file = "pics/smallkeys.gif")
    data.picBigKeys = PhotoImage(file = "pics/bigkeys.gif")
    data.picMetro = PhotoImage(file = "pics/metronome.gif")
    data.instrumentToPic = {"Drums": data.picDrums, "Synth": data.picSynth,
                            "Voice": data.picVoice}

    data.musicDrums = "sounds/beats/BDRUM13.wav"
    data.synthNotesToMusic = {}
    data.musicMetro = "sounds/metroBeat.wav"

    data.numberOfRecorded = [] # list of instruments recorded
    data.recordCircleColour = data.blue05
    data.isAudio = False
    data.drumsRecorded = [] # 2d list of times of drum beats recorded
    data.drumsDrawingTimes = [] # 2d list of whether there was a beat every 50ms
    data.synthsRecordedTime = [] #2d list of times of synth notes recorded
    data.synthsRecordedNotes = [] #2d list of notes of synth notes recorded
    data.synthsDrawingTimes = []
    data.voicesRecorded = []
    data.voicesDrawingTimes = []
    data.drawAudioTrackSpacesD = [] # pos of last track
    data.drawAudioTrackSpacesS = []
    data.drawAudioTrackSpacesV = []

    data.currentRecordingSynthNotes = []
    data.currentRecordingTime = []
    data.currentDrawingTimes = []
    data.synthNotePlaying = 0
    data.voiceRecordingTime = 1000

    data.drumTrackDrawingBlocks = []
    data.synthTrackDrawingBlocks = []
    data.voiceTrackDrawingBlocks = []
    data.drumBlockSelected = "poptarts"
    data.synthBlockSelected = "eggtarts"
    data.voiceBlockSelected = "sweettarts"

    data.metronomeBPM = 80
    data.recordEndSpaceAudioBars = 380
    data.replayOffset = 0
    data.replayingAllCounter = 0
    data.drumMetroCounter = "cheetos"
    data.synthMetroCounter = "fishballs"
    data.voiceMetroCounter = "cries"
    data.recordEndCounter = 0
    data.recordEndPlayBar = 127

    data.isReplaying = False
    data.seenInstrumentsToPic = {}
    data.seenInstruments = {}
    data.offset = 0

######################### MODE DISPATCHER ##########################

def mousePressed(event, data):
    if (data.mode == "main"): mainMousePressed(event, data)
    elif (data.mode == "play"): playMousePressed(event, data)
    elif (data.mode == "playAddInstrument"): 
        playAddInstrumentMousePressed(event, data)
    elif (data.mode == "playAddDrums"): playAddDrumsMousePressed(event, data)
    elif (data.mode == "recordDrumsStart"): 
        recordDrumsStartMousePressed(event, data)
    elif (data.mode == "recordEnd"): recordEndMousePressed(event, data)
    elif (data.mode == "playAddSynth"): playAddSynthMousePressed(event, data)
    elif (data.mode == "recordSynthStart"): 
        recordSynthStartMousePressed(event, data)
    elif (data.mode == "playAddVoice"): playAddVoiceMousePressed(event, data)
    elif (data.mode == "recordVoiceStart"): recordVoiceStartMousePressed(event, data)
    elif (data.mode == "playAddDrumsMetro"): playAddDrumsMetroMousePressed(event, data)
    elif (data.mode == "playAddSynthMetro"): playAddSynthMetroMousePressed(event, data)
    elif (data.mode == "playAddVoiceMetro"): playAddVoiceMetroMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "main"): mainKeyPressed(event, data)
    elif (data.mode == "play"): playKeyPressed(event, data)
    elif (data.mode == "playAddInstrument"): 
        playAddInstrumentKeyPressed(event, data)
    elif (data.mode == "playAddDrums"): playAddDrumsKeyPressed(event, data)
    elif (data.mode == "recordDrumsStart"): 
        recordDrumsStartKeyPressed(event, data)
    elif (data.mode == "recordEnd"): recordEndKeyPressed(event, data)
    elif (data.mode == "playAddSynth"): playAddSynthKeyPressed(event, data)
    elif (data.mode == "recordSynthStart"): 
        recordSynthStartKeyPressed(event, data)
    elif (data.mode == "playAddVoice"): playAddVoiceKeyPressed(event, data)
    elif (data.mode == "recordVoiceStart"): recordVoiceStartKeyPressed(event, data)
    elif (data.mode == "playAddDrumsMetro"): playAddDrumsMetroKeyPressed(event, data)
    elif (data.mode == "playAddSynthMetro"): playAddSynthMetroKeyPressed(event, data)
    elif (data.mode == "playAddVoiceMetro"): playAddVoiceMetroKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "main"): mainTimerFired(data)
    elif (data.mode == "play"): playTimerFired(data)
    elif (data.mode == "playAddInstrument"): playAddInstrumentTimerFired(data)
    elif (data.mode == "playAddDrums"): playAddDrumsTimerFired(data)
    elif (data.mode == "recordDrumsStart"): recordDrumsStartTimerFired(data)
    elif (data.mode == "recordEnd"):
        recordEndTimer= thr.Thread(target = recordEndTimerFired, args = (data,))
        recordEndTimer.start()
    elif (data.mode == "playAddSynth"): playAddSynthTimerFired(data)
    elif (data.mode == "recordSynthStart"): recordSynthStartTimerFired(data)
    elif (data.mode == "playAddVoice"): playAddVoiceTimerFired(data)
    elif (data.mode == "recordVoiceStart"): recordVoiceStartTimerFired(data)
    elif (data.mode == "playAddDrumsMetro"): playAddDrumsMetroTimerFired(data)
    elif (data.mode == "playAddSynthMetro"): playAddSynthMetroTimerFired(data)
    elif (data.mode == "playAddVoiceMetro"): playAddVoiceMetroTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "main"): mainRedrawAll(canvas, data)
    elif (data.mode == "play"): playRedrawAll(canvas, data)
    elif (data.mode == "playAddInstrument"): 
        playAddInstrumentRedrawAll(canvas, data)
    elif (data.mode == "playAddDrums"): playAddDrumsRedrawAll(canvas, data)
    elif (data.mode == "recordDrumsStart"): 
        recordDrumsStartRedrawAll(canvas, data)
    elif (data.mode == "recordEnd"): recordEndRedrawAll(canvas, data)
    elif (data.mode == "playAddSynth"): playAddSynthRedrawAll(canvas, data)
    elif (data.mode == "recordSynthStart"): 
        recordSynthStartRedrawAll(canvas, data)
    elif (data.mode == "playAddVoice"): playAddVoiceRedrawAll(canvas, data)
    elif (data.mode == "recordVoiceStart"): recordVoiceStartRedrawAll(canvas, data)
    elif (data.mode == "playAddDrumsMetro"): playAddDrumsMetroRedrawAll(canvas, data)
    elif (data.mode == "playAddSynthMetro"): playAddSynthMetroRedrawAll(canvas, data)
    elif (data.mode == "playAddVoiceMetro"): playAddVoiceMetroRedrawAll(canvas, data)

########################## RUN FUNCTION ############################

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