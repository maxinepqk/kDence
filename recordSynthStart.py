########################## RECORD SYNTH START SCREEN ###########################
import time
from audiofunctions import playMusic
from recordDrumsStart import getDrawAudioSpacing, getTrackDrawingBlockDims
import threading as thr
from audio import play

def recordSynthStartMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    if (event.x > 157 and event.x < 1040 and event.y > 102 and event.y < 596):
        if (event.x > 165 and event.x < 506 and event.y > 211 and event.y < 575): # oct 0
            if ((event.x > 163 and event.x < 192 and event.y > 208 and event.y <434) or
                (event.x > 163 and event.x < 209 and event.y > 434 and event.y < 573)):
                data.synthNotePlaying = "C0"
            elif (event.x > 192 and event.x < 220 and event.y > 210 and event.y < 433):
                data.synthNotePlaying = "C#0"
            elif ((event.x > 222 and event.x < 250 and event.y >210 and event.y<436) or
                 (event.x > 212 and event.x < 259 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "D0"
            elif (event.x > 252 and event.x < 284 and event.y > 211 and event.y < 436):
                data.synthNotePlaying = "D#0"
            elif ((event.x > 283 and event.x < 308 and event.y >210 and event.y<436) or
                 (event.x > 261 and event.x < 305 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "E0"
            elif ((event.x > 310 and event.x < 335 and event.y >210 and event.y<436) or
                 (event.x > 307 and event.x < 355 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "F0"
            elif (event.x > 336 and event.x < 367 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "F#0"
            elif ((event.x > 364 and event.x < 388 and event.y >210 and event.y<436) or
                 (event.x > 358 and event.x < 403 and event.y > 405 and event.y < 576)):
                data.synthNotePlaying = "G0"
            elif (event.x > 392 and event.x < 419 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "G#0"
            elif ((event.x > 422 and event.x < 446 and event.y >210 and event.y<436) or
                 (event.x > 407 and event.x < 455 and event.y > 436 and event.y < 576)):
                data.synthNotePlaying = "A0"
            elif (event.x > 447 and event.x < 478 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "A#0"
            elif ((event.x > 479 and event.x < 501 and event.y >210 and event.y<436) or
                 (event.x > 457 and event.x < 502 and event.y > 436 and event.y < 576)):
                data.synthNotePlaying = "B0"
            data.isAudio = "0"
        elif (event.x > 505 and event.x < 842 and event.y > 211 and event.y < 575): # oct 1
            if ((event.x > 163+340 and event.x < 192+340 and event.y > 208 and event.y <434) or
                (event.x > 163+340 and event.x < 209+340 and event.y > 434 and event.y < 573)):
                data.synthNotePlaying = "C1"
            elif (event.x > 192+340 and event.x < 220+340 and event.y > 210 and event.y < 433):
                data.synthNotePlaying = "C#1"
            elif ((event.x > 222+340 and event.x < 250+340 and event.y >210 and event.y<436) or
                 (event.x > 212+340 and event.x < 259+340 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "D1"
            elif (event.x > 252+340 and event.x < 284+340 and event.y > 211 and event.y < 436):
                data.synthNotePlaying = "D#1"
            elif ((event.x > 283+340 and event.x < 308+340 and event.y >210 and event.y<436) or
                 (event.x > 261+340 and event.x < 305+340 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "E1"
            elif ((event.x > 310+340 and event.x < 335+340 and event.y >210 and event.y<436) or
                 (event.x > 307+340 and event.x < 355+340 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "F1"
            elif (event.x > 336+340 and event.x < 367+340 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "F#1"
            elif ((event.x > 364+340 and event.x < 388+340 and event.y >210 and event.y<436) or
                 (event.x > 358+340 and event.x < 403+340 and event.y > 405 and event.y < 576)):
                data.synthNotePlaying = "G1"
            elif (event.x > 392+340 and event.x < 419+340 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "G#1"
            elif ((event.x > 422+340 and event.x < 446+340 and event.y >210 and event.y<436) or
                 (event.x > 407+340 and event.x < 455+340 and event.y > 436 and event.y < 576)):
                data.synthNotePlaying = "A1"
            elif (event.x > 447+340 and event.x < 478+340 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "A#1"
            elif ((event.x > 479+340 and event.x < 501+340 and event.y >210 and event.y<436) or
                 (event.x > 457+340 and event.x < 502+340 and event.y > 436 and event.y < 576)):
                data.synthNotePlaying = "B1"
            data.isAudio = "1"
        elif (event.x > 841):
            if ((event.x > 163+340*2 and event.x < 192+340*2 and event.y > 208 and event.y <434) or
                (event.x > 163+340*2 and event.x < 209+340*2 and event.y > 434 and event.y < 573)):
                data.synthNotePlaying = "C2"
            elif (event.x > 192+340*2 and event.x < 220+340*2 and event.y > 210 and event.y < 433):
                data.synthNotePlaying = "C#2"
            elif ((event.x > 222+340*2 and event.x < 250+340*2 and event.y >210 and event.y<436) or
                 (event.x > 212+340*2 and event.x < 259+340*2 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "D2"
            elif (event.x > 252+340*2 and event.x < 284+340*2 and event.y > 211 and event.y < 436):
                data.synthNotePlaying = "D#2"
            elif ((event.x > 283+340*2 and event.x < 308+340*2 and event.y >210 and event.y<436) or
                 (event.x > 261+340*2 and event.x < 305+340*2 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "E2"
            elif ((event.x > 310+340*2 and event.x < 335+340*2 and event.y >210 and event.y<436) or
                 (event.x > 307+340*2 and event.x < 355+340*2 and event.y > 434 and event.y < 576)):
                data.synthNotePlaying = "F2"
            elif (event.x > 336+340*2 and event.x < 367+340*2 and event.y > 210 and event.y < 436):
                data.synthNotePlaying = "F#2"
            data.isAudio = "2"
        data.currentRecordingTime.append(time.time())
        data.currentRecordingSynthNotes.append(data.synthNotePlaying)
        data.music = data.synthNotesToMusic[data.synthNotePlaying]
        playMusic(data)

    elif (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "playAddSynth" # clicked the back button
    else:
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Synth")
        data.synthsRecordedTime.append(data.currentRecordingTime)
        data.synthsRecordedNotes.append(data.currentRecordingSynthNotes)
        data.synthsDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)

def recordSynthStartKeyPressed(event, data):
    if (event.keysym == "Return"): 
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Synth")
        data.synthsRecordedTime.append(data.currentRecordingTime)
        data.synthsRecordedNotes.append(data.currentRecordingSynthNotes)
        data.synthsDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)
    else:
        if (event.keysym == "z" or event.keysym == "s" or event.keysym == "x"
            or event.keysym == "d" or event.keysym == "c" or event.keysym=="v"
            or event.keysym == "g" or event.keysym == "b" or event.keysym=="h"
            or event.keysym == "n" or event.keysym == "j" 
            or event.keysym=="m"):
            if (event.keysym == "z"): data.synthNotePlaying = "C0"
            elif (event.keysym == "s"): data.synthNotePlaying = "C#0"
            elif (event.keysym == "x"): data.synthNotePlaying = "D0"
            elif (event.keysym == "d"): data.synthNotePlaying = "D#0"
            elif (event.keysym == "c"): data.synthNotePlaying = "E0"
            elif (event.keysym == "v"): data.synthNotePlaying = "F0"
            elif (event.keysym == "g"): data.synthNotePlaying = "F#0"
            elif (event.keysym == "b"): data.synthNotePlaying = "G0"
            elif (event.keysym == "h"): data.synthNotePlaying = "G#0"
            elif (event.keysym == "n"): data.synthNotePlaying = "A0"
            elif (event.keysym == "j"): data.synthNotePlaying = "A#0"
            elif (event.keysym == "m"): data.synthNotePlaying = "B0"
            data.isAudio = "0"
        elif (event.keysym == "q" or event.keysym == "2" or event.keysym == "w"
            or event.keysym == "3" or event.keysym == "e" or event.keysym=="r"
            or event.keysym == "5" or event.keysym == "t" or event.keysym=="6"
            or event.keysym == "y" or event.keysym == "7" 
            or event.keysym=="u"):
            if (event.keysym == "q"): data.synthNotePlaying = "C1"
            elif (event.keysym == "2"): data.synthNotePlaying = "C#1"
            elif (event.keysym == "w"): data.synthNotePlaying = "D1"
            elif (event.keysym == "3"): data.synthNotePlaying = "D#1"
            elif (event.keysym == "e"): data.synthNotePlaying = "E1"
            elif (event.keysym == "r"): data.synthNotePlaying = "F1"
            elif (event.keysym == "5"): data.synthNotePlaying = "F#1"
            elif (event.keysym == "t"): data.synthNotePlaying = "G1"
            elif (event.keysym == "6"): data.synthNotePlaying = "G#1"
            elif (event.keysym == "y"): data.synthNotePlaying = "A1"
            elif (event.keysym == "7"): data.synthNotePlaying = "A#1"
            elif (event.keysym == "u"): data.synthNotePlaying = "B1"
            data.isAudio = "1"
        elif (event.keysym == "i" or event.keysym == "9" or event.keysym == "o"
            or event.keysym == "0" or event.keysym == "p" or event.keysym=="k"
            or event.keysym == "l"):
            if (event.keysym == "i"): data.synthNotePlaying = "C2"
            elif (event.keysym == "9"): data.synthNotePlaying = "C#2"
            elif (event.keysym == "o"): data.synthNotePlaying = "D2"
            elif (event.keysym == "0"): data.synthNotePlaying = "D#2"
            elif (event.keysym == "p"): data.synthNotePlaying = "E2"
            elif (event.keysym == "k"): data.synthNotePlaying = "F2"
            elif (event.keysym == "l"): data.synthNotePlaying = "F#2"
            data.isAudio = "2"
        data.currentRecordingTime.append(time.time())
        data.currentRecordingSynthNotes.append(data.synthNotePlaying)
        data.music = data.synthNotesToMusic[data.synthNotePlaying]
        playMusic(data)
  
def recordSynthStartTimerFired(data):
    data.recordCounter += 1
    # drawing for audio bars
    if (isinstance(data.isAudio, str)): 
        data.currentDrawingTimes.append(data.isAudio)
        data.isAudio = False
    else:
        data.currentDrawingTimes.append(False)
    t = int((60 / data.metronomeBPM)*10)
    if (not isinstance(data.synthMetroCounter, str)):
        if (data.recordCounter % t == 0):
            playingMetro = thr.Thread(target = play, args = (data.musicMetro,))
            playingMetro.start()

def recordSynthStartRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    canvas.create_image(data.cx, data.cy-50, image = data.picBigKeys)
    canvas.create_text(data.cx, data.cy + 250, 
                       text = "Hit keys to record a tune!",
                       font = ("Lato Thin Italic", 40), fill = data.blue4)
    canvas.create_text(data.cx, data.cy+300, 
                       text = "Click outside the keyboard or hit enter to " + 
                       "stop recording!", font = ("Lato Thin Italic", 30),
                       fill = data.blue4)