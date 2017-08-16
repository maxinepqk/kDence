########################## RECORD END SCREEN ###########################

from play import playDrawButtons
from audiofunctions import (replayMusic, replayMelody, replayDrums, replaySynth,
replayVoice)
import threading as thr
from threading import Lock
from audio import play
from helperfunctions import swap, saveVars, loadVars
from recordDrumsStart import getDrawAudioSpacing, getTrackDrawingBlockDims
import os

def replayAllMusic(data):
    data.recordEndCounter = 0
    data.offset = 0
    data.recordEndPlayBar = 127

    (drumCount, data.synthCount, voiceCount) = (-1, -1, -1)
    for instrument in data.numberOfRecorded:
        if (instrument == "Drums"):
            data.music = data.musicDrums
            drumCount += 1
            data.currentPlaying = data.drumsRecorded[drumCount]
            replayMusic(data)
            #replayingDrums = thr.Thread(target = replayMusic, args = (data,))
            #replayingDrums.start()
        elif (instrument == "Synth"):
            data.synthCount += 1
            data.currentPlaying = data.synthsRecordedTime[data.synthCount]
            data.music = data.synthNotesToMusic[data.synthNotePlaying]
            replayMelody(data)
            # replayingSynth = thr.Thread(target = replayMusic, args = (data,))
            # replayingSynth.start()
        elif(instrument == "Voice"):
            voiceCount += 1
            data.music = data.voicesRecorded[voiceCount]
            play(data.music)
            # replayingVoice = thr.Thread(target = play, args = (data.music,))
            # replayingVoice.start()
    data.isReplaying = False

    ## I tried replaying all instruments at once using multithreading, spent
    ## a long time researching it and experimenting with locks, but 
    ## multi-threading acted so irrationally that it was inconsistent each time,
    ## so I just decided to go back playing them in order

    # if ("Drums" in data.numberOfRecorded):
    #     data.musicD = data.musicDrums
    #     replayingDrums = thr.Thread(target = replayDrums, args = (data,))
    #     replayingDrums.start()
        
    # if("Synth" in data.numberOfRecorded):
    #     replayingSynth = thr.Thread(target = replaySynth, args = (data,))
    #     replayingSynth.start()

    # if("Voice" in data.numberOfRecorded):
    #     replayingVoice = thr.Thread(target = replayVoice, args = (data,))
    #     replayingVoice.start()
        

def recordEndMousePressed(event, data):
    
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR)
    (playx0, playy0, playx1, playy1) = (data.cx-15, 8, data.cx+15, 38)
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr) 
    (savex0, savey0, savex1, savey1, saver) = (backx0, backy0+backr*3, backx1, 
                                               backy1+backr*3, backr)
    (pausex0, pausey0, pausex1, pausey1) = (data.cx-100, 13, data.cx-78, 38)
    if (event.x > addx0 and event.x < addx1 and event.y > addy0 and 
        event.y < addy1):
        data.mode = "playAddInstrument" # clicked the add button
    elif (event.x > playx0 and event.x < playx1 and event.y > playy0 and 
        event.y < playy1):
        data.isReplaying = True
        replayingAllMusic = thr.Thread(target = replayAllMusic, args = (data,))
        replayingAllMusic.start()
    elif (event.x > backx0 and event.x < backx1 and event.y > backy0 
        and event.y < backy1):
        data.mode = "main" # clicked the back button
    elif (event.x > savex0 and event.x < savex1 and event.y > savey0 
        and event.y < savey1):
        saveVars(data) # clicked the save button
    # elif (event.x > pausex0 and event.x < pausex1 and event.y > pausey0 
    #     and event.y < pausey1):
    #     data.isReplaying = False

    if (data.drumTrackDrawingBlocks != []):
        for drumBlock in data.drumTrackDrawingBlocks:
            (blockx0, blocky1, blockx1, blocky0) = drumBlock
            if (event.x > blockx0 and event.x < blockx1 and event.y > blocky0 and
                event.y < blocky1):
                data.drumBlockSelected = data.drumTrackDrawingBlocks.index(drumBlock)
    if (data.synthTrackDrawingBlocks != []):
        for synthBlock in data.synthTrackDrawingBlocks:
            (blockx0, blocky1, blockx1, blocky0) = synthBlock
            if (event.x > blockx0 and event.x < blockx1 and event.y > blocky0 and
                event.y < blocky1):
                data.synthBlockSelected = data.synthTrackDrawingBlocks.index(synthBlock)
    if (data.voiceTrackDrawingBlocks != []):
        for voiceBlock in data.voiceTrackDrawingBlocks:
            (blockx0, blocky1, blockx1, blocky0) = voiceBlock
            if (event.x > blockx0 and event.x < blockx1 and event.y > blocky0 and
                event.y < blocky1):
                data.voiceBlockSelected = data.voiceTrackDrawingBlocks.index(voiceBlock)

def recordEndKeyPressed(event, data):
    if (event.keysym == "Left"  or event.keysym == "Right"):
        if (not isinstance(data.drumBlockSelected, str)):
            if (event.keysym == "Left"):
                if (data.drumBlockSelected != 0): 
                    swap(data.drumsRecorded, data.drumBlockSelected-1,
                         data.drumBlockSelected)
                    swap(data.drumsDrawingTimes, data.drumBlockSelected-1,
                         data.drumBlockSelected)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.drumBlockSelected = "cinnamonroll"
            elif (event.keysym == "Right"):
                if (data.drumBlockSelected != len(data.drumTrackDrawingBlocks) - 1):
                    swap(data.drumsRecorded, data.drumBlockSelected,
                         data.drumBlockSelected + 1)
                    swap(data.drumsDrawingTimes, data.drumBlockSelected,
                         data.drumBlockSelected + 1)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.drumBlockSelected = "chasiewbao"

        if (not isinstance(data.synthBlockSelected, str)):
            if (event.keysym == "Left"):
                if (data.synthBlockSelected != 0): 
                    swap(data.synthsRecordedTime, data.synthBlockSelected-1,
                         data.synthBlockSelected)
                    swap(data.synthsRecordedNotes, data.synthBlockSelected-1,
                         data.synthBlockSelected)
                    swap(data.synthsDrawingTimes, data.synthBlockSelected-1,
                         data.synthBlockSelected)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.synthBlockSelected = "matchawarabimochi"
            elif (event.keysym == "Right"):
                if (data.synthBlockSelected != len(data.synthTrackDrawingBlocks) - 1):
                    swap(data.synthsRecordedTime, data.synthBlockSelected,
                         data.synthBlockSelected+1)
                    swap(data.synthsRecordedNotes, data.synthBlockSelected,
                         data.synthBlockSelected+1)
                    swap(data.synthsDrawingTimes, data.synthBlockSelected,
                         data.synthBlockSelected+1)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.synthBlockSelected = "iwantfood"

        if (not isinstance(data.voiceBlockSelected, str)):
            if (event.keysym == "Left"):
                if (data.voiceBlockSelected != 0): 
                    swap(data.voicesRecorded, data.voiceBlockSelected-1,
                         data.voiceBlockSelected)
                    swap(data.voicesDrawingTimes, data.voiceBlockSelected-1,
                         data.voiceBlockSelected)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.voiceBlockSelected = "cinnamonroll"
            elif (event.keysym == "Right"):
                if (data.voiceBlockSelected != len(data.voiceTrackDrawingBlocks) - 1):
                    swap(data.voicesRecorded, data.voiceBlockSelected,
                         data.voiceBlockSelected + 1)
                    swap(data.voicesDrawingTimes, data.voiceBlockSelected,
                         data.voiceBlockSelected + 1)
                    getDrawAudioSpacing(data)
                    getTrackDrawingBlockDims(data)
                    data.mode = "recordEnd"
                    data.voiceBlockSelected = "chasiewbao"


def recordEndTimerFired(data):
    #data.recordEndCounter += 1
    if (data.isReplaying):
        #data.recordEndPlayBar += 10
        data.recordEndCounter += 100
        if (data.recordEndCounter >= 380):
            data.offset -= 1

def drawAudioBars(canvas, data):
    (x0, barW, barMaxH, barMinH, spc) = (140+data.offset, 5, 50, 10, 2)
    data.seenInstruments = dict()
    instrumRow = -1
    data.spaceW = data.width-data.playButtonR*2-19
    (drumI, synthI, voiceI, trackI, instrumentI)= (-1, -1, -1, -1, -1)
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
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10, 
                fill = data.blue15, width = 0) # block of each track
            else:
                data.needToDrawMore = True
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10, 
                fill = data.blue15, width = 0)

            for dIsAudio in currentD:
                dI += 1
                x1 = x0+barW*(dI+1)+currTrackSpc
                if (dIsAudio == True):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+dI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMaxH, 
                        fill = data.blue5, width = 0)
                else:
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+dI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMinH, 
                        fill = data.blue5, width = 0)


        elif (instrument == "Synth"):
            synthI += 1
            currentS = data.synthsDrawingTimes[synthI]
            sI = -1
            lastsI = len(currentS) - 1
            blockx1 = x0+lastsI*barW+spc+currTrackSpc+7
            if (blockx1 < data.spaceW):
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10, 
                fill = data.blue15, width = 0) # block of each track
            else:
                data.needToDrawMore = True
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10, 
                fill = data.blue15, width = 0)

            for sIsAudio in currentS:
                sI += 1
                x1 = x0+barW*(sI+1)+currTrackSpc
                if (not isinstance(sIsAudio, str)):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMinH, 
                        fill = data.blue5, width = 0)
                elif (sIsAudio == "0"):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x1, y0-(barMaxH-barMinH)//3, 
                        fill = data.blue5, width = 0)
                elif (sIsAudio == "1"):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x1, y0-((barMaxH-barMinH)*2)//3, 
                        fill = data.blue5, width = 0)
                elif (sIsAudio == "2"):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMaxH, 
                        fill = data.blue5, width = 0)

        elif(instrument == "Voice"):
            voiceI += 1
            currentV = data.voicesDrawingTimes[voiceI]
            vI = -1
            lastvI = len(currentV) - 1
            blockx1 = x0+lastvI*barW+spc+currTrackSpc+7
            if (blockx1 < data.spaceW):
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                blockx1, y0-barMaxH-10, 
                fill = data.blue15, width = 0) # block of each track
            else:
                data.needToDrawMore = True
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                data.spaceW, y0-barMaxH-10, 
                fill = data.blue15, width = 0)

            for vIsAudio in currentV:
                vI += 1
                x1 = x0+barW*(vI+1)+currTrackSpc
                if (vIsAudio == True):
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+vI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMaxH, 
                        fill = data.blue5, width = 0)
                else:
                    if (x1 < data.spaceW):
                        canvas.create_rectangle(x0+vI*barW+spc+currTrackSpc, y0, 
                        x1, y0-barMinH, 
                        fill = data.blue5, width = 0)

def recordEndDrawSpace(canvas, data):
    canvas.create_rectangle(120, 5, data.width-data.playButtonR*2-12, 
                            data.height, fill = data.blue05, width = 0) # space
    canvas.create_rectangle(5, 5, 120, data.height, fill = data.blue07, 
                            width = 0) # sidebar
    canvas.create_rectangle(5, 5, data.width-data.playButtonR*2-12, 50, 
                            fill = data.blue0, width = 0) # top bar
    canvas.create_polygon(data.cx-15, 8, data.cx-15, 38, data.cx+15, 23, 
                          activefill = data.blue4, fill = data.blue3, width = 0) #play
    # canvas.create_rectangle(data.cx-100, 13, data.cx-78, 38, activefill=data.blue4,
    #                         fill = data.blue3, width = 0) # pause button
    # canvas.create_rectangle(data.cx-93, 13, data.cx-85, 38, fill=data.blue0,
    #                         width = 0)

def recordEndDrawButtons(canvas, data):
    (addx0, addy0, addx1, addy1, addr) = (data.width-data.playButtonR*2-5, 8, 
                                          data.width-5, 8+data.playButtonR*2, 
                                          data.playButtonR) 
    (backx0, backy0, backx1, backy1, backr) = (addx0, addy0+addr*3, addx1, 
                                               addy1+addr*3, addr)

    (savex0, savey0, savex1, savey1, saver) = (backx0, backy0+backr*3, backx1, 
                                               backy1+backr*3, backr)
    canvas.create_oval(savex0, savey0, savex1, savey1, activefill = data.blue3,
                       fill = data.blue2, width = 0)
    canvas.create_line((savex0+savex1)//2, savey0+10, (savex0+savex1)//2, 
                        savey1-10, fill = data.blue0, width = 0) # vert
    canvas.create_line(savex0+10, (savey0+savey1)//2-3, (savex0+savex1)//2,
                       savey1-10, fill = data.blue0, width = 0)
    canvas.create_line((savex0+savex1)//2, savey1-10, savex1-10,
                       (savey0+savey1)//2-3, fill = data.blue0, width = 0)

def recordEndDrawSideBar(canvas, data):
    canvas.create_rectangle(5, 50, 120, data.height, fill = data.blue07, 
                            width = 0) # sidebar
    canvas.create_rectangle(120, 50, 127, data.height, fill = data.blue05, width = 0)
    data.seenInstrumentsPic = {}
    instrumRow = -1

    for instrument in data.numberOfRecorded: # draws out toolbar

        if (instrument not in data.seenInstrumentsPic):
            instrumRow = len(set(data.seenInstrumentsPic))
            data.seenInstrumentsPic[instrument] = instrumRow
        else:
            instrumRow = data.seenInstrumentsPic[instrument]
        y0 = 100 + instrumRow * 100
        canvas.create_image(60, y0, 
                            image = data.instrumentToPic[instrument])
    
def recordEndDrawPlayBar(canvas, data):
    if (data.isReplaying):
        canvas.create_line(data.recordEndPlayBar, 50, data.recordEndPlayBar, 
                           data.height, fill = data.blue5, width = 0)

def recordEndRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    recordEndDrawSpace(canvas, data)
    playDrawButtons(canvas, data)
    recordEndDrawButtons(canvas, data)
    drawAudioBars(canvas, data)
    #recordEndDrawPlayBar(canvas, data)
    recordEndDrawSideBar(canvas, data)
