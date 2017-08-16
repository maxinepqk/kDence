import os, os.path, json

def rgbString(red, green, blue): # taken from course notes
    return "#%02x%02x%02x" % (red, green, blue)

def almostEqual(d1, d2, epsilon=10**-6): # cited from cs112_f16 test code
    return (abs(d2 - d1) < epsilon)

def almostLessThanOrEqual(d1, d2, epsilon=10**-6):
    return ((d1 - d2) < epsilon) # test for d1 <= d2

def swap(a, i, j): # taken from course notes
    (a[i], a[j]) = (a[j], a[i])

# saveVars and loadVars functions adapted from http://bit.ly/2gxzBXB
def saveVars(data):
    number =  str(len([name for name in os.listdir("savedFiles") 
               if os.path.isfile(name)])) # this line is from bit.ly/2gx1QWl
    saveFileName = "savedFiles/1.json"
    jsonSerializedVars = json.dumps(
                        {"data.drawAudioTrackSpaces": data.drawAudioTrackSpaces,
                         "data.numberOfRecorded": data.numberOfRecorded,
                         "data.voicesRecorded": data.voicesRecorded,
                         "data.voicesDrawingTimes": data.voicesDrawingTimes,
                         "data.drumTrackDrawingBlocks": data.drumTrackDrawingBlocks,
                         "data.synthTrackDrawingBlocks": data.synthTrackDrawingBlocks,
                         "data.currentRecordingSynthNotes": data.currentRecordingSynthNotes,
                         "data.currentRecordingTime": data.currentRecordingTime,
                         "data.currentDrawingTimes": data.currentDrawingTimes,
                         "data.drawAudioTrackSpaces": data.drawAudioTrackSpaces,
                         "data.drumsRecorded": data.drumsRecorded,
                         "data.drumsDrawingTimes": data.drumsDrawingTimes,
                         "data.synthsRecordedTime": data.synthsRecordedTime,
                         "data.synthsDrawingTimes": data.synthsDrawingTimes,
                         "data.synthNotesToMusic": data.synthNotesToMusic,
                         "data.synthNotePlaying": data.synthNotePlaying,
                         "data.synthsRecordedNotes": data.synthsRecordedNotes,
                         "data.seenInstruments": data.seenInstruments,
                         "data.seenInstrumentsToPic": data.seenInstrumentsToPic})
    fn = open(saveFileName, "w")
    fn.write(jsonSerializedVars)
    fn.close()

def loadVars(data):
    number =  str(len([name for name in os.listdir("savedFiles") 
               if os.path.isfile(name)])) # this line is from bit.ly/2gx1QWl
    
    saveFileName = "savedFiles/1.json"
    if(os.path.isfile(saveFileName)):
        fn = open(saveFileName)
    jsonVars= json.loads(fn.read())
    fn.close()
    data.numberOfRecorded = jsonVars["data.numberOfRecorded"]
    data.drawAudioTrackSpaces = jsonVars["data.drawAudioTrackSpaces"]
    data.numberOfRecorded = jsonVars["data.numberOfRecorded"]
    data.voicesRecorded = jsonVars["data.voicesRecorded"]
    data.voicesDrawingTimes = jsonVars["data.voicesDrawingTimes"]
    data.drumTrackDrawingBlocks = jsonVars["data.drumTrackDrawingBlocks"]
    data.synthTrackDrawingBlocks = jsonVars["data.synthTrackDrawingBlocks"]
    data.currentRecordingSynthNotes = jsonVars["data.currentRecordingSynthNotes"]
    data.currentRecordingTime = jsonVars["data.currentRecordingTime"]
    data.currentDrawingTimes = jsonVars["data.currentDrawingTimes"]
    data.drawAudioTrackSpaces = jsonVars["data.drawAudioTrackSpaces"]
    data.drumsRecorded = jsonVars["data.drumsRecorded"]
    data.drumsDrawingTimes = jsonVars["data.drumsDrawingTimes"]
    data.synthsRecordedTime = jsonVars["data.synthsRecordedTime"]
    data.synthsDrawingTimes = jsonVars["data.synthsDrawingTimes"]
    data.synthNotesToMusic = jsonVars["data.synthNotesToMusic"]
    data.synthNotePlaying = jsonVars["data.synthNotePlaying"]
    data.synthsRecordedNotes = jsonVars["data.synthsRecordedNotes"]
    data.seenInstruments = jsonVars["data.seenInstruments"]
    data.seenInstrumentsToPic = jsonVars["data.seenInstrumentsToPic"]