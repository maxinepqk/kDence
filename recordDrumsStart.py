########################## RECORD DRUMS START SCREEN ##########################
from audiofunctions import playMusic
import time
import threading as thr
from play import playDrawButtons
from audio import play

def recordDrumsStartMousePressed(event, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    if (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "playAddDrums" # clicked the back button
    else:
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Drums")
        data.drumsRecorded.append(data.currentRecordingTime)
        data.drumsDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)

def recordDrumsStartKeyPressed(event, data):
    if (event.keysym == "space"):
        playMusic(data)
        data.currentRecordingTime.append(time.time())
        data.isAudio = True

    elif (event.keysym == "Return"):
        data.mode = "recordEnd"
        data.offset = 0
        data.needToDrawMore = False
        data.numberOfRecorded.append("Drums")
        data.drumsRecorded.append(data.currentRecordingTime)
        data.drumsDrawingTimes.append(data.currentDrawingTimes)
        getDrawAudioSpacing(data)
        getTrackDrawingBlockDims(data)

def recordDrumsStartTimerFired(data):
    data.recordCounter += 1
    if (data.recordCounter % 3 == 0): # make em flash
        if (data.recordCircleColour == data.blue05):
            data.recordCircleColour = data.blue2
        else: data.recordCircleColour = data.blue05
    # drawing for audio bars
    if (data.isAudio == True): 
        data.currentDrawingTimes.append(True)
        data.isAudio = False
    else:
        data.currentDrawingTimes.append(False)
    t = int((60 / data.metronomeBPM)*10)
    if (not isinstance(data.drumMetroCounter, str)):
        if (data.recordCounter % t == 0):
            playingMetro = thr.Thread(target = play, args = (data.musicMetro,))
            playingMetro.start()

def recordDrumsStartDrawCircle(canvas, data):
    (cx, cy, r) = (data.cx, data.cy-30, 30)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = data.recordCircleColour,
                       width = 0)

def recordDrumsStartRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    recordDrumsStartDrawCircle(canvas, data)
    playDrawButtons(canvas, data)
    canvas.create_text(data.cx, data.cy+30, 
                       text = "Click anywhere on the screen or hit enter to " + 
                       "stop recording!", font = ("Lato Thin Italic", 30),
                       fill = data.blue4)

def getDrawAudioSpacing(data):
    (x0, barW) = (140, 5)
    (drumI, synthI, voiceI)= (-1, -1, -1)
    data.drawAudioTrackSpaces = []
    for instrument in data.numberOfRecorded:
        
        if (instrument == "Drums"):
            drumI += 1
            currentD = data.drumsDrawingTimes[drumI]
            lastdI = len(currentD) - 1
            newSpace = x0 + barW*lastdI
            data.drawAudioTrackSpaces.append(newSpace)

        elif (instrument == "Synth"):
            synthI += 1
            currentS = data.synthsDrawingTimes[synthI]
            lastsI = len(currentS) - 1
            newSpace = x0 + barW*lastsI
            data.drawAudioTrackSpaces.append(newSpace)

        elif(instrument == "Voice"):
            voiceI += 1
            currentV = data.voicesDrawingTimes[voiceI]
            lastvI = len(currentV) - 1
            newSpace = x0 + barW*lastvI
            data.drawAudioTrackSpaces.append(newSpace)

def getTrackDrawingBlockDims(data):
    # (x0, barW, barMaxH, barMinH, spc) = (140, 5, 50, 10, 2)
    # seenInstruments = dict()
    # instrumRow = -1
    # (data.drumTrackDrawingBlocks, data.synthTrackDrawingBlocks, 
    # data.voiceTrackDrawingBlocks) = ([],[], [])

    # for instrument in data.numberOfRecorded:

    #     if (instrument not in seenInstruments):
    #         instrumRow += 1
    #         seenInstruments[instrument] = instrumRow
    #     else:
    #         instrumRow = seenInstruments[instrument]
    #     y0 = 120 + instrumRow * 100
    #     trackI = -1

    #     if (instrument == "Drums"):
    #         for dtrack in data.drumsDrawingTimes:
    #             trackI += 1
    #             if (trackI > 0):
    #                 currTrackSpc = (sum(data.drawAudioTrackSpaces[:trackI])
    #                                 -110*trackI)
    #             else:
    #                 currTrackSpc = sum(data.drawAudioTrackSpaces[:trackI])
    #             lastdI = len(dtrack)
    #             (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, 
    #             y0+10, x0+lastdI*barW+spc+currTrackSpc+7, y0-barMaxH-10)
    #             data.drumTrackDrawingBlocks.append((blockx0, blocky0,
    #             blockx1, blocky1))

    #     elif (instrument == "Synth"):
    #         for strack in data.synthsDrawingTimes:
    #             trackI += 1
    #             if (trackI > 0):
    #                 currTrackSpc = (sum(data.drawAudioTrackSpaces[:trackI])
    #                                 -110*trackI)
    #             else:
    #                 currTrackSpc = sum(data.drawAudioTrackSpaces[:trackI])
    #             lastsI = len(strack)
    #             (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, 
    #             y0+10, x0+lastsI*barW+spc+currTrackSpc+7, y0-barMaxH-10)
    #             data.synthTrackDrawingBlocks.append((blockx0, blocky0,
    #             blockx1, blocky1))

    #     elif (instrument == "Voice"):
    #         for vtrack in data.voicesDrawingTimes:
    #             trackI += 1
    #             if (trackI > 0):
    #                 currTrackSpc = (sum(data.drawAudioTrackSpaces[:trackI])
    #                                 -110*trackI)
    #             else:
    #                 currTrackSpc = sum(data.drawAudioTrackSpaces[:trackI])
    #             lastvI = len(vtrack)
    #             (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, 
    #             y0+10, x0+lastvI*barW+spc+currTrackSpc+7, y0-barMaxH-10)
    #             data.voiceTrackDrawingBlocks.append((blockx0, blocky0,
    #             blockx1, blocky1))
    
    (x0, barW, barMaxH, barMinH, spc) = (140+data.offset, 5, 50, 10, 2)
    data.seenInstruments = dict()
    instrumRow = -1
    data.spaceW = data.width-data.playButtonR*2-19
    (drumI, synthI, voiceI, trackI, instrumentI)= (-1, -1, -1, -1, -1)
    (data.drumTrackDrawingBlocks, data.synthTrackDrawingBlocks, 
    data.voiceTrackDrawingBlocks) = ([],[], [])
    for instrument in data.numberOfRecorded:
        instrumentI += 1
        currTrackSpc = (sum(data.drawAudioTrackSpaces[:instrumentI])
                                    -110*instrumentI)

        if (instrument not in data.seenInstruments):
            instrumRow = len(set(data.seenInstruments))
            data.seenInstruments[instrument] = instrumRow
        else:
            instrumRow = data.seenInstruments[instrument]
        y0 = 120 + instrumRow * 100
        
        if (instrument == "Drums"):
            drumI += 1
            currentD = data.drumsDrawingTimes[drumI]
            dI = -1
            lastdI = len(currentD) - 1
            blockx1 = x0+lastdI*barW+spc+currTrackSpc+7
            if (blockx1 < data.spaceW):
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10)
            else:
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10)
            data.drumTrackDrawingBlocks.append((blockx0, blocky0,
            blockx1, blocky1))

        elif (instrument == "Synth"):
            synthI += 1
            currentS = data.synthsDrawingTimes[synthI]
            sI = -1
            lastsI = len(currentS) - 1
            blockx1 = x0+lastsI*barW+spc+currTrackSpc+7
            if (blockx1 < data.spaceW):
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10)
            else:
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10)
            data.synthTrackDrawingBlocks.append((blockx0, blocky0,
            blockx1, blocky1))

        elif(instrument == "Voice"):
            voiceI += 1
            currentV = data.voicesDrawingTimes[voiceI]
            vI = -1
            lastvI = len(currentV) - 1
            blockx1 = x0+lastvI*barW+spc+currTrackSpc+7
            if (blockx1 < data.spaceW):
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10)
            else:
                (blockx0, blocky0, blockx1, blocky1) = (x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10)
            data.voiceTrackDrawingBlocks.append((blockx0, blocky0,
            blockx1, blocky1))