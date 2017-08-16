############################ MAIN SCREEN #############################
from helperfunctions import loadVars

def mainMousePressed(event, data):
    (startX, startY) = data.startButtonPos
    (openX, openY) = data.openButtonPos
    if (event.x > startX - 37 and event.x < startX + 37 and
        event.y > startY - 18 and event.y < startY + 18):
        data.mode = "play" # clicked start
    elif (event.x > openX - 37 and event.x < openX + 37 and
        event.y > openY - 18 and event.y < openY + 18):
        loadVars(data)
        data.mode = "recordEnd"

def mainKeyPressed(event, data): pass

def mainTimerFired(data): pass

def mainRedrawAll(canvas, data):
    canvas.create_image(data.cx, data.cy, image = data.picBG) # background
    canvas.create_text(data.cx, data.cy - 40, text = "kDence", 
                       font = ("Lato Thin", 100), fill = data.blue4) # title
    canvas.create_text(data.startButtonPos, activefill = data.blue2, 
                       text = "start", font = ("Lato Thin Italic", 40), 
                       fill = data.blue3) # start button
    canvas.create_text(data.openButtonPos, activefill = data.blue2, 
                       text = "open", font = ("Lato Thin Italic", 40), 
                       fill = data.blue3) # open button
    # canvas.create_text(data.helpButtonPos, activefill = data.blue2, 
    #                    text = "help", font = ("Lato Thin Italic", 40), 
    #                    fill = data.blue3) # help button