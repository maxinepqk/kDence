##########################  PLAY ADD VOICE SCREEN ###########################
from play import playDrawButtons
from playAddInstrument import playAddInstrumentDrawStaticMenu
from audio import record, play
import threading as thr
from drawingfunctions import drawMetronome, drawMetroMenu

def playAddVoiceMetroMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr)
    (metrox0, metroy0, metrox1, metroy1) = (25, data.height-95, 95, 
                                            data.height-25)
    (metroupx0, metroupy0, metroupx1, metroupy1) = (metrox1+25, metroy0,
                                                    metrox1+55, metroy0+15)
    (metrodwnx0, metrodwny0, metrodwnx1, metrodwny1) = (metrox1+25, metroy1-15,
                                                        metrox1+55, metroy1) 
    if (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "playAddInstrument" # clicked the back button
    elif (event.x > metrox0 and event.x < metrox1 and event.y > metroy0 and
          event.y < metroy1):
        data.mode = "playAddVoice"
    elif (event.x > metroupx0 and event.x < metroupx1 and event.y > metroupy0 
          and event.y < metroupy1):
        data.metronomeBPM += 10
    elif (event.x > metrodwnx0 and event.x < metrodwnx1 and 
          event.y > metrodwny0 and event.y < metrodwny1):
        data.metronomeBPM -= 10
        if (data.metronomeBPM < 0): data.metronomeBPM = 0.1

def playAddVoiceMetroKeyPressed(event, data):
    if (event.keysym == "space"):
        data.recordCounter = 0
        data.currRecordingVoice = "recordings/%d.wav"%len(data.voicesRecorded)
        data.mode = "recordVoiceStart"
        data.currentDrawingTimes = []
        recording= thr.Thread(target = record, args = (data,))
        recording.start()

def playAddVoiceMetroTimerFired(data):
    data.voiceMetroCounter += 1
    t = int((60 / data.metronomeBPM)*10)
    if (data.voiceMetroCounter % t == 0):
        playingMetro = thr.Thread(target = play, args = (data.musicMetro,))
        playingMetro.start()

def playAddVoiceDrawInstructs(canvas, data):
    (cx, cy) = (data.cx - 60, data.cy)
    canvas.create_text(cx, cy-40, text = "%s selected!" %data.currentInstrument,
                       font = ("Lato Thin", 60), fill = data.blue4)
    canvas.create_text(cx, cy+20, text = "Hit space to start recording",
                       font = ("Lato Thin Italic", 35), fill = data.blue3)
    canvas.create_text(cx, cy+60, text = "Adjust the metronome speed with arrows",
                       font = ("Lato Thin Italic", 25), fill = data.blue3)

def playAddVoiceDrawMenu(canvas, data):
    (x0, y0, x1, y1, r) = (data.width-data.playButtonR*2-5, 8, data.width-5, 
                           8+data.playButtonR*2, data.playButtonR)
    canvas.create_rectangle(x0-115, y0+205, x0-15, y0+300, 
                            activefill = data.blue07, fill = data.blue05, 
                            width = 0)
    playAddInstrumentDrawStaticMenu(canvas, data)

def playAddVoiceMetroRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    playDrawButtons(canvas, data)
    playAddVoiceDrawMenu(canvas, data)
    playAddVoiceDrawInstructs(canvas, data)
    drawMetronome(canvas, data)
    drawMetroMenu(canvas, data)