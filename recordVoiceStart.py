########################## RECORD VOICE START SCREEN ##########################
from recordDrumsStart import recordDrumsStartDrawCircle
from recordDrumsStart import getDrawAudioSpacing, getTrackDrawingBlockDims
import threading as thr
from audio import play

def recordVoiceStartMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    if (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "playAddVoice" # clicked the back button
    else:
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Voice")
        data.voicesRecorded.append(data.currRecordingVoice)
        data.voicesDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)      

def recordVoiceStartKeyPressed(event, data):
    if (event.keysym == "Return"):
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Voice")
        data.voicesRecorded.append(data.currRecordingVoice) 
        data.voicesDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)

def recordVoiceStartTimerFired(data):
    data.recordCounter += 1
    if (data.recordCounter % 3 == 0): # make em flash
        if (data.recordCircleColour == data.blue05):
            data.recordCircleColour = data.blue2
        else: data.recordCircleColour = data.blue05
    elif(data.recordCounter % 5 == 0):
        data.currentDrawingTimes.append(True)
    else:
        data.currentDrawingTimes.append(False)
    t = int((60 / data.metronomeBPM)*10)
    if (not isinstance(data.voiceMetroCounter, str)):
        if (data.recordCounter % t == 0):
            playingMetro = thr.Thread(target = play, args = (data.musicMetro,))
            playingMetro.start()

def recordVoiceStartRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    canvas.create_text(data.cx, data.cy+30, 
                   text = "Click anywhere on the screen or hit enter to " + 
                   "stop recording!", font = ("Lato Thin Italic", 30),
                   fill = data.blue4)
    recordDrumsStartDrawCircle(canvas, data)