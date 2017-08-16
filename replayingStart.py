########################## REPLAYING START SCREEN ###########################
from recordEnd import (recordEndMousePressed, recordEndKeyPressed, 
recordEndRedrawAll, drawAudioBars, recordEndDrawSpace)
from play import playDrawButtons
from audiofunctions import replayMusic, replayMelody
import threading as thr
from audio import play
from helperfunctions import swap, saveVars, loadVars
from recordDrumsStart import getDrawAudioSpacing, getTrackDrawingBlockDims
import os

def replayingStartMousePressed(event, data):
    recordEndMousePressed(event, data)

def replayingStartKeyPressed(event, data):
    recordEndKeyPressed(event, data)

def replayingStartTimerFired(data):
    data.replayingAllCounter += 1
    if (data.replayingAllCounter > 380):
        data.replayOffset += 5

def replayDrawAudioBars(canvas, data):
    (x0, barW, barMaxH, barMinH, spc) = (140, 5, 50, 10, 2)
    seenInstruments = dict()
    instrumRow = -1
    data.spaceW = data.width-data.playButtonR*2-19
    
    for instrument in data.numberOfRecorded:

        if (instrument not in seenInstruments):
            instrumRow += 1
            seenInstruments[instrument] = instrumRow
        else:
            instrumRow = seenInstruments[instrument]
        y0 = 120 + instrumRow * 100
        trackI = -1
        # allI = -1
        if (instrument == "Drums"):
            for dtrack in data.drumsDrawingTimes:
                trackI += 1
                #allI += 1
                if (trackI > 0):
                    currTrackSpc = (sum(data.drawAudioTrackSpaces[:trackI])
                                    -110*trackI)
                else:
                    currTrackSpc = sum(data.drawAudioTrackSpaces[:trackI])
                dI = -1
                lastdI = len(dtrack)
                blockx1 = x0+lastdI*barW+spc+currTrackSpc+7
                if (blockx1 < data.spaceW):
                    canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                    blockx1, y0-barMaxH-10, 
                    fill = data.blue15, width = 0) # block of each track
                else:
                    canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                    data.spaceW, y0-barMaxH-10, 
                    fill = data.blue15, width = 0)
                for dIsAudio in dtrack:
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
            for strack in data.synthsDrawingTimes:
                trackI += 1
                #allI += 1
                if (trackI > 0):
                    currTrackSpc = (sum(data.drawAudioTrackSpaces[:trackI])
                                    -110*trackI)
                else:
                    currTrackSpc = sum(data.drawAudioTrackSpaces[:trackI])
                sI = -1
                lastsI = len(strack)
                canvas.create_rectangle(x0+currTrackSpc-7, y0+10, 
                x0+lastsI*barW+spc+currTrackSpc+7, y0-barMaxH-10, 
                fill = data.blue15, width = 0) # block of each track
                for sIsAudio in strack:
                    sI += 1
                    if (sIsAudio == "0"):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x0+barW*(sI+1)+currTrackSpc, int(y0-(barMaxH-barMinH)/3), 
                        fill = data.blue5, width = 0)
                    elif (sIsAudio == "1"):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x0+barW*(sI+1)+currTrackSpc, int(y0-(barMaxH-barMinH)*2/3), 
                        fill = data.blue5, width = 0)
                    elif (sIsAudio == "2"):
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x0+barW*(sI+1)+currTrackSpc, y0-barMaxH, fill = data.blue5,
                        width = 0)
                    else:
                        canvas.create_rectangle(x0+sI*barW+spc+currTrackSpc, y0, 
                        x0+barW*(sI+1)+currTrackSpc, y0-barMinH, fill = data.blue5, 
                        width = 0)

        elif (instrument == "Voice"):
            vI = -1
            for vIsAudio in data.voicesDrawingTimes:
                vI += 1
                if (vIsAudio == True):
                    canvas.create_rectangle(x0+vI*barW+spc, y0, 
                    x0+barW*(vI+1), y0-barMaxH, 
                    fill = data.blue5, width = 0)
                else:
                    canvas.create_rectangle(x0+vI*barW+spc, y0, 
                    x0+barW*(vI+1), y0-barMinH, 
                    fill = data.blue5, width = 0)

def replayingStartRedrawAll(canvas, data):
    recordEndRedrawAll(canvas, data)