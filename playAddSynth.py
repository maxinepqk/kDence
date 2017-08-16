########################## PLAY ADD SYNTH SCREEN ###########################

from play import playDrawButtons
from playAddInstrument import playAddInstrumentDrawStaticMenu
from drawingfunctions import drawMetronome
from audiofunctions import replayMetronome
import threading as thr
import time

def playAddSynthMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr)
    (metrox0, metroy0, metrox1, metroy1) = (25, data.height-95, 95, 
                                            data.height-25) 
    if (event.x > 245 and event.x < 833 and event.y > 409 and event.y < 648):
        data.recordCounter = 0
        data.currentRecordingSynthNotes = []
        data.currentRecordingTime = [time.time()]
        data.currentDrawingTimes = []
        data.isAudio = False
        data.mode = "recordSynthStart"
    elif (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "playAddInstrument" # clicked the back button
    elif (event.x > metrox0 and event.x < metrox1 and event.y > metroy0 and
          event.y < metroy1):
        data.synthMetroCounter = 0
        data.mode = "playAddSynthMetro"

def playAddSynthKeyPressed(event, data): pass

def playAddSynthTimerFired(data): pass

def playAddSynthDrawInstructs(canvas, data):
    (cx, cy) = (data.cx - 60, data.cy)
    canvas.create_text(cx, cy-200, text = "%s selected!" 
                       %data.currentInstrument, font = ("Lato Thin", 60), 
                       fill = data.blue4)
    canvas.create_text(cx, cy-140, 
                       text = "Hit the keys below to start recording!",
                       font = ("Lato Thin Italic", 35), fill = data.blue3)
    canvas.create_text(cx, cy-100, text = "Click the metronome to turn it on",
                       font = ("Lato Thin Italic", 25), fill = data.blue3)
    canvas.create_image(cx, cy+100, image = data.picSmallKeys)

def playAddSynthDrawMenu(canvas, data):
    (x0, y0, x1, y1, r) = (data.width-data.playButtonR*2-5, 8, data.width-5, 
                           8+data.playButtonR*2, data.playButtonR)
    canvas.create_rectangle(x0-115, y0+105, x0-15, y0+200,  fill = data.blue07, 
                            width = 0)
    playAddInstrumentDrawStaticMenu(canvas, data)

def playAddSynthRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    playDrawButtons(canvas, data)
    playAddSynthDrawMenu(canvas, data)
    playAddSynthDrawInstructs(canvas, data)
    drawMetronome(canvas, data)