###################### PLAY ADD INSTRUMENT SCREEN #######################

from play import playDrawButtons
from recordEnd import recordEndDrawSpace

def makeSynthNotesToMusic(data):
    notes = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", 
             "A#0", "B0", "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1",
             "G#1", "A1", "A#1", "B1", "C2", "C#2", "D2", "D#2", "E2", "F2", 
             "F#2"]
    for note in notes:
        data.synthNotesToMusic[note] = "sounds/notes/%s.wav" %note

def playAddInstrumentMousePressed(event, data):
    data.currentRecordingTime = []
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    if (event.x > addx0 and event.x < addx1 and event.y > addy0 
        and event.y < addy1):
        data.mode = "play" # clicked the add button to minimize
    elif (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "play" # clicked the back button
    elif (event.x > addx0-115 and event.x < addx0-15 and  event.y > addy0+5 and 
          event.y < addy0+100): # drums
        data.mode = "playAddDrums"
        data.currentInstrument = "Drums"
    elif (event.x > addx0-115 and event.x < addx0-15 and  event.y > addy0+105 and 
          event.y < addy0+205): # synth
        data.mode = "playAddSynth"
        data.currentInstrument = "Synth"
        makeSynthNotesToMusic(data)
    elif (event.x > addx0-115 and event.x < addx0-15 and  event.y > addy0+205 and 
          event.y < addy0+305): # voice
        data.mode = "playAddVoice"
        data.currentInstrument = "Voice"


def playAddInstrumentKeyPressed(event, data): pass

def playAddInstrumentTimerFired(data): pass

def playAddInstrumentDrawMenu(canvas, data):
    (x0, y0, x1, y1, r) = (data.width-data.playButtonR*2-5, 8, data.width-5, 
                           8+data.playButtonR*2, data.playButtonR)
    canvas.create_rectangle(x0-120, y0, x0-10, data.height, fill = data.blue05, 
                            width = 0) # main menu
    canvas.create_rectangle(x0-115, y0+5, x0-15, y0+100, 
                            activefill = data.blue07, fill = data.blue05, 
                            width = 0)
    canvas.create_image(x0-60, y0+50, image = data.picDrums)
    canvas.create_rectangle(x0-115, y0+105, x0-15, y0+200, 
                            activefill = data.blue07, fill = data.blue05, 
                            width = 0)
    canvas.create_image(x0-60, y0+150, image = data.picSynth)
    canvas.create_rectangle(x0-115, y0+205, x0-15, y0+300, 
                            activefill = data.blue07, fill = data.blue05, 
                            width = 0)
    canvas.create_image(x0-60, y0+250, image = data.picVoice)


def playAddInstrumentRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    playDrawButtons(canvas, data)
    if (data.numberOfRecorded != []): 
        recordEndDrawSpace(canvas, data)
    playAddInstrumentDrawMenu(canvas, data)

def playAddInstrumentDrawStaticMenu(canvas, data):
    (x0, y0, x1, y1, r) = (data.width-data.playButtonR*2-5, 8, data.width-5, 
                           8+data.playButtonR*2, data.playButtonR)
    canvas.create_rectangle(x0-120, y0, x0-10, data.height, fill = data.blue05, 
                            width = 0) # main menu
    canvas.create_image(x0-60, y0+50, image = data.picDrums)
    canvas.create_image(x0-60, y0+150, image = data.picSynth)
    canvas.create_image(x0-60, y0+250, image = data.picVoice)

