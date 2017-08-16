from tkinter import *
import time, decimal
import threading as thr
from threading import Lock 
from audio import play
from helperfunctions import almostEqual, almostLessThanOrEqual

## AUDIO FUNCTIONS

def playMusic(data):
    playing = thr.Thread(target = play, args = (data.music,))
    playing.start()

def playMusicD(data):
    playingD = thr.Thread(target = play, args = (data.musicD,))
    playingD.start()

def playMusicS(data):
    playingS = thr.Thread(target = play, args = (data.musicS,))
    playingS.start()

# def playMusicV(data):
    # playingV = thr.Thread(target = play, args = (data.musicV,))
    # playingV.start()

def getTimeDiff(data):
    data.tDiff = [] 
    for i in range(len(data.currentPlaying)):
        t = data.currentPlaying[i] - data.currentPlaying[i-1]
        data.tDiff.append(t) # gets the difference in time

def getTimeDiffD(data):
    data.tDiffD = [] 
    for i in range(len(data.currentPlayingD)):
        t = data.currentPlayingD[i] - data.currentPlayingD[i-1]
        data.tDiffD.append(t) # gets the difference in time

def getTimeDiffS(data):
    data.tDiffS = [] 
    for i in range(1, len(data.currentPlayingS)):
        t = data.currentPlayingS[i] - data.currentPlayingS[i-1]
        data.tDiffS.append(t) # gets the difference in time

def replayMusic(data):
    getTimeDiff(data) # returns a list of time differences between each beat
    for t in data.tDiff:
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playMusic(data)
                break

def replayMusicD(data):
    getTimeDiffD(data) # returns a list of time differences between each beat
    for t in data.tDiffD:
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playMusicD(data)
                break

def replayMelody(data):
    i = -1
    getTimeDiff(data)
    data.music = data.synthNotesToMusic[data.synthsRecordedNotes[data.synthCount][0]]
    for t in data.tDiff[1:]:
        i += 1
        data.music = data.synthNotesToMusic[data.synthsRecordedNotes[data.synthCount][i]]
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playMusic(data)
                break

def replayMetronome(data):
    t = 60 / data.metronomeBPM
    tNow = time.time()
    while (data.mode == "playAddDrumsMetro" or data.mode == "recordDrumsStart" or
           data.mode == "playAddSynthMetro" or data.mode == "recordSynthStart" or
           data.mode == "playAddVoiceMetro" or data.mode == "recordVoiceStart"): 
        tNow = time.time()
        while(almostLessThanOrEqual(time.time(), tNow + t)):
            if almostEqual(time.time(), tNow + t):
                playingMetro = thr.Thread(target = play, args = (data.musicMetro,))
                playingMetro.start()
                break

def replayDrums(data): # sets which track is playing
    print(data.drumsRecorded)
    data.lock.acquire()
    for drumCount in range(len(data.drumsRecorded)):
        data.currentPlayingD = data.drumsRecorded[drumCount]
        replayMusicD(data)
    data.lock.release()

def replaySynth(data): # sets which track is playing
    data.synthCount = -1
    data.lock.acquire()
    for synthCount in range(len(data.synthsRecordedTime)):
        data.synthCount += 1
        data.currentPlayingS = data.synthsRecordedTime[data.synthCount]
        #data.musicS = data.synthNotesToMusic[data.synthNotePlaying]
        replayMelody(data)
    data.lock.release()

def replayVoice(data):
    for voiceCount in data.voicesRecorded:
        data.musicV = voiceCount
        play(data.musicV)




    